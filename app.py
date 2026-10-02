"""
Flask Live Application for the 90-Day Transformation Challenge
Full real-time interactive web project with 3D Visualizations, Live 100% Gauge,
Diet Planner, and Punishment Chamber.
"""

import json
import os
import random
import webbrowser
from datetime import datetime
from threading import Timer
from flask import Flask, jsonify, render_template, request  # type: ignore
import plotly.graph_objects as go  # type: ignore
from plotly.subplots import make_subplots  # type: ignore
import numpy as np  # type: ignore
import fitness_engine as fe
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, "templates")

app = Flask(__name__, template_folder=template_dir)
handler = app

@app.route("/")
def index():
    progress = fe.load_progress()
    current_day = progress.get("current_day", 1)
    user_prof = progress.get("user_profile", {
        "weight_kg": 74.0, "height_cm": 175.0, "age": 25, "gender": "male", "activity_level": "moderate"
    })
    macros = fe.NutritionEngine.calculate_macros(
        weight_kg=user_prof["weight_kg"],
        height_cm=user_prof["height_cm"],
        age=user_prof["age"],
        gender=user_prof["gender"],
        activity_level=user_prof["activity_level"]
    )
    meal_plan = fe.NutritionEngine.get_meal_plan()
    return render_template("index.html", 
                           current_day=current_day, 
                           user_prof=user_prof, 
                           macros=macros,
                           meal_plan=meal_plan)

@app.route("/api/day/<int:day>")
def get_day(day):
    routine_info = fe.get_day_routine(day)
    progress = fe.load_progress()
    completed_today = progress.get("completed_workouts", {}).get(str(day), [])
    
    # Enrich exercises with database details
    enriched_exercises = []
    for ex in routine_info["exercises"]:
        name = ex["name"]
        db_info = fe.EXERCISE_DATABASE.get(name, {})
        enriched_exercises.append({
            "name": name,
            "sets": ex["sets"],
            "reps": ex["reps"],
            "rest_sec": ex["rest_sec"],
            "target_area": db_info.get("target_area", "Full Body"),
            "muscle": db_info.get("muscle", "Core / Glutes"),
            "burn": db_info.get("cals_per_min", 8.0),
            "description": db_info.get("description", ""),
            "animation_id": db_info.get("animation_id", "hip_thrusts"),
            "joint_focus": db_info.get("joint_focus", "Form and alignment"),
            "tempo": db_info.get("tempo", "3-1-1-0"),
            "primary_muscle": db_info.get("primary_muscle", db_info.get("muscle", "Target Muscle")),
            "secondary_muscle": db_info.get("secondary_muscle", "Core / Stabilizers"),
            "form_steps": db_info.get("form_steps", []),
            "mistakes_to_avoid": db_info.get("mistakes_to_avoid", []),
            "completed": name in completed_today
        })
    
    return jsonify({
        "day": day,
        "phase": routine_info["phase"],
        "phase_title": routine_info["phase_title"],
        "routine_name": routine_info["routine_name"],
        "focus": routine_info["focus"],
        "exercises": enriched_exercises
    })

@app.route("/api/exercises")
def get_all_exercises():
    """Returns the full exercise repertoire with video clips, form cues, and muscle targets."""
    return jsonify(fe.EXERCISE_DATABASE)

@app.route("/api/analyze_physique", methods=["POST"])
def analyze_physique():
    data = request.json or {}
    image_b64 = data.get("image", "")
    scan_type = data.get("scan_type", "full_body")
    
    progress = fe.load_progress()
    user_prof = progress.get("user_profile", {"weight_kg": 74.0, "height_cm": 175.0, "age": 25})
    
    result = fe.PhysiqueAnalyzer.analyze_image_data(image_b64, scan_type=scan_type, user_stats=user_prof)
    
    # Save scan history
    progress.setdefault("physique_scans", []).append({
        "timestamp": result["scan_timestamp"],
        "scan_type": scan_type,
        "scores": result["scores"],
        "action_plan": [p["what_to_do"] for p in result["prescriptions"]]
    })
    fe.save_progress(progress)
    
    return jsonify(result)

@app.route("/api/evaluate", methods=["POST"])
def evaluate_workout():
    data = request.json or {}
    day = int(data.get("day", 1))
    completed_exercises = data.get("completed", [])
    total_count = int(data.get("total", len(completed_exercises)))
    is_preview = bool(data.get("preview", False))
    
    progress = fe.load_progress()
    
    if not is_preview:
        progress.setdefault("completed_workouts", {})[str(day)] = completed_exercises
        progress["current_day"] = day
        
        eval_result = fe.PunishmentManager.evaluate_workout(len(completed_exercises), total_count, day)
        
        if eval_result["punished"] and eval_result.get("debt_record"):
            progress.setdefault("punishment_ledger", []).append(eval_result["debt_record"])
            
        fe.save_progress(progress)
    else:
        # Preview / render charts mode: Do NOT save or assign penalties
        eval_result = fe.PunishmentManager.evaluate_workout(len(completed_exercises), total_count, day)
    
    # 1. 100% Completion Gauge JSON
    fig_gauge, pct, is_comp = fe.create_completion_meter(len(completed_exercises), total_count, day)
    gauge_json = fig_gauge.to_dict()
    
    # 2. 3D Graphs JSON
    fig_topo = fe.generate_3d_muscle_topology(completed_exercises, day)
    fig_surf = fe.generate_3d_performance_surface(completed_exercises, day)
    fig_traj = fe.generate_3d_90day_trajectory(day)
    
    topo_json = fig_topo.to_dict()
    surf_json = fig_surf.to_dict()
    traj_json = fig_traj.to_dict()
    
    return jsonify({
        "success": True,
        "day": day,
        "completed_count": len(completed_exercises),
        "total_count": total_count,
        "pct": pct,
        "is_complete": is_comp,
        "evaluation": eval_result,
        "gauge": gauge_json,
        "topo_3d": topo_json,
        "surf_3d": surf_json,
        "traj_3d": traj_json
    })

@app.route("/api/workout/reset_day", methods=["POST"])
def reset_day_workout():
    data = request.json or {}
    day = int(data.get("day", 1))
    
    progress = fe.load_progress()
    if "completed_workouts" in progress and str(day) in progress["completed_workouts"]:
        progress["completed_workouts"][str(day)] = []
    
    # Clean up unpaid accidental punishments for this day
    if "punishment_ledger" in progress:
        progress["punishment_ledger"] = [
            p for p in progress["punishment_ledger"]
            if not (p.get("day") == day and not p.get("paid", False))
        ]
        
    fe.save_progress(progress)
    return jsonify({
        "success": True,
        "day": day,
        "message": f"Day {day} workout has been reset. All exercises and sets are fresh and ready to start!"
    })

@app.route("/api/calculate_macros", methods=["POST"])
def calculate_macros():
    data = request.json or {}
    weight = float(data.get("weight_kg", 74.0))
    height = float(data.get("height_cm", 175.0))
    age = int(data.get("age", 25))
    gender = str(data.get("gender", "male"))
    activity = str(data.get("activity_level", "moderate"))
    
    # Update profile in progress
    progress = fe.load_progress()
    progress["user_profile"] = {
        "weight_kg": weight, "height_cm": height, "age": age, "gender": gender, "activity_level": activity
    }
    fe.save_progress(progress)
    
    macros = fe.NutritionEngine.calculate_macros(weight, height, age, gender, activity)
    
    # Macro Donut Chart JSON
    fig_macro = go.Figure(data=[go.Pie(
        labels=['Protein (Muscle Repair)', 'Healthy Fats (Hormones)', 'Complex Carbs (Energy)'],
        values=[macros['protein_g']*4, macros['fat_g']*9, macros['carbs_g']*4],
        hole=.5,
        marker_colors=['#00FF88', '#FFB800', '#00F0FF']
    )])
    fig_macro.update_layout(
        template="plotly_dark",
        height=320,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="#161B22",
        plot_bgcolor="#161B22"
    )
    
    return jsonify({
        "macros": macros,
        "macro_chart": fig_macro.to_dict()
    })

@app.route("/api/punishment_roulette")
def punishment_roulette():
    tier = random.choice(["minor", "moderate", "severe"])
    pun = random.choice(fe.PUNISHMENT_TIERS[tier])
    return jsonify({
        "tier": tier,
        "punishment": pun
    })

@app.route("/api/ledger")
def get_ledger():
    progress = fe.load_progress()
    return jsonify(progress.get("punishment_ledger", []))

@app.route("/api/pay_debt", methods=["POST"])
def pay_debt():
    idx = request.json.get("index")
    progress = fe.load_progress()
    ledger = progress.get("punishment_ledger", [])
    if 0 <= idx < len(ledger):
        ledger[idx]["paid"] = True
        progress["punishment_ledger"] = ledger
        fe.save_progress(progress)
        return jsonify({"success": True, "message": "Debt paid! Honor restored."})
    return jsonify({"success": False, "message": "Invalid index."}), 400

@app.route("/api/log_measurement", methods=["POST"])
def log_measurement():
    data = request.json or {}
    day = int(data.get("day", 1))
    weight = float(data.get("weight_kg", 74.0))
    waist = float(data.get("waist_cm", 85.0))
    hips = float(data.get("hips_cm", 98.0))
    
    progress = fe.load_progress()
    progress.setdefault("weight_history", []).append({
        "day": day,
        "weight_kg": weight,
        "waist_cm": waist,
        "hips_cm": hips,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    fe.save_progress(progress)
    
    # Generate progress chart
    history = progress["weight_history"]
    days = [h["day"] for h in history]
    weights = [h["weight_kg"] for h in history]
    waists = [h["waist_cm"] for h in history]
    hips_list = [h["hips_cm"] for h in history]
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=days, y=waists, name="Waist (Belly Fat)", line=dict(color="#00F0FF", width=3)), secondary_y=False)
    fig.add_trace(go.Scatter(x=days, y=hips_list, name="Glutes (Butt Muscle)", line=dict(color="#FF007F", width=3)), secondary_y=False)
    fig.add_trace(go.Scatter(x=days, y=weights, name="Weight (kg)", line=dict(color="#FFB800", width=2, dash="dot")), secondary_y=True)
    
    fig.update_layout(
        title_text="<b>90-DAY PROGRESSION: WAIST REDUCTION VS GLUTE HYPERTROPHY</b>",
        template="plotly_dark",
        height=380,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="#161B22",
        plot_bgcolor="#161B22"
    )
    return jsonify({
        "success": True,
        "chart": fig.to_dict()
    })

@app.route("/api/vitals", methods=["GET"])
def get_vitals():
    day = request.args.get("day", default=1, type=int)
    progress = fe.load_progress()
    report = fe.VitalsEngine.get_full_vitals_report(progress, day=day)
    return jsonify(report)

@app.route("/api/vitals/update", methods=["POST"])
def update_vitals():
    data = request.json or {}
    day = int(data.get("day", 1))
    progress = fe.load_progress()
    vitals = progress.setdefault("vitals", {})

    if "heart_rate_bpm" in data:
        vitals["heart_rate_bpm"] = int(data["heart_rate_bpm"])
    if "resting_hr_bpm" in data:
        vitals["resting_hr_bpm"] = int(data["resting_hr_bpm"])
    if "blood_oxygen_pct" in data:
        vitals["blood_oxygen_pct"] = float(data["blood_oxygen_pct"])
    if "blood_pressure_sys" in data:
        vitals["blood_pressure_sys"] = int(data["blood_pressure_sys"])
    if "blood_pressure_dia" in data:
        vitals["blood_pressure_dia"] = int(data["blood_pressure_dia"])
    if "hrv_ms" in data:
        vitals["hrv_ms"] = int(data["hrv_ms"])
    if "daily_steps" in data:
        vitals["daily_steps"] = int(data["daily_steps"])
    if "active_calories" in data:
        vitals["active_calories"] = float(data["active_calories"])

    fe.save_progress(progress)
    report = fe.VitalsEngine.get_full_vitals_report(progress, day=day)
    return jsonify({
        "success": True,
        "message": "Biometric vitals successfully synced & updated!",
        "report": report
    })

@app.route("/api/workout/calc_hr_zone", methods=["POST"])
def calc_hr_zone():
    data = request.json or {}
    bpm = int(data.get("bpm", 120))
    age = int(data.get("age", 25))
    zone_info = fe.WorkoutSessionManager.calculate_heart_rate_zone(bpm, age)
    return jsonify(zone_info)

@app.route("/api/workout/live_gauge", methods=["POST"])
def live_gauge():
    data = request.json or {}
    completed_sets = int(data.get("completed_sets", 0))
    total_sets = int(data.get("total_sets", 1))
    cals = float(data.get("active_calories", 0.0))
    fig = fe.WorkoutSessionManager.create_live_set_gauge(completed_sets, total_sets, cals)
    return jsonify({
        "gauge": fig.to_dict(),
        "pct": round((completed_sets / total_sets) * 100) if total_sets > 0 else 0
    })

@app.route("/api/workout/save_session", methods=["POST"])
def save_session():
    data = request.json or {}
    day = int(data.get("day", 1))
    duration_sec = int(data.get("duration_sec", 0))
    active_calories = float(data.get("active_calories", 0.0))
    avg_hr = int(data.get("avg_hr", 125))
    sets_logged = data.get("sets_logged", [])
    completed_exercises = data.get("completed_exercises", [])
    total_exercises = int(data.get("total_exercises", len(completed_exercises)))
    
    progress = fe.load_progress()
    session_record = {
        "day": day,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "duration_min": round(duration_sec / 60.0, 1),
        "active_calories": active_calories,
        "avg_hr": avg_hr,
        "total_sets": len(sets_logged),
        "sets_detail": sets_logged
    }
    progress.setdefault("workout_sessions", []).append(session_record)
    progress.setdefault("completed_workouts", {})[str(day)] = completed_exercises
    fe.save_progress(progress)
    
    return jsonify({
        "success": True,
        "message": f"Workout Session saved! {round(duration_sec/60, 1)} mins | {active_calories:.0f} kcal burned."
    })

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 90-DAY BODY TRANSFORMATION LIVE SUITE IS STARTING!")
    print("👉 Serving locally at: http://127.0.0.1:5000")
    print("="*60 + "\n")
    Timer(1.5, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
