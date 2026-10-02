"""
Generate a complete, self-contained interactive HTML Dashboard of the
90-Day Body Transformation Challenge (Day 1 Demo with 3D Visuals & Completion Gauge).
"""

import os
import fitness_engine as fe
import plotly.graph_objects as go  # type: ignore

def build_dashboard_html(day=1, save_path="dashboard_preview.html"):
    routine = fe.get_day_routine(day)
    macros = fe.NutritionEngine.calculate_macros(74.0, 175.0, 25, "male", "moderate")
    all_ex_names = [e["name"] for e in routine["exercises"]]
    
    # 1. 100% Completion Gauge
    fig_gauge, pct, is_comp = fe.create_completion_meter(len(all_ex_names), len(all_ex_names), day)
    
    # 2. 3D Graphs
    fig_topo = fe.generate_3d_muscle_topology(all_ex_names, day)
    fig_surf = fe.generate_3d_performance_surface(all_ex_names, day)
    fig_traj = fe.generate_3d_90day_trajectory(day)
    
    # 3. Macro Donut
    fig_macro = go.Figure(data=[go.Pie(
        labels=['Protein (Muscle Growth)', 'Healthy Fats (Hormones)', 'Complex Carbs (Energy)'],
        values=[macros['protein_g']*4, macros['fat_g']*9, macros['carbs_g']*4],
        hole=.45,
        marker_colors=['#00FF88', '#FFB800', '#00B4D8']
    )])
    fig_macro.update_layout(
        title_text="<b>DAILY RECOMPOSITION MACRO SPLIT</b>",
        template="plotly_dark",
        height=320,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="#161B22",
        plot_bgcolor="#161B22"
    )

    gauge_html = fig_gauge.to_html(full_html=False, include_plotlyjs='cdn')
    topo_html = fig_topo.to_html(full_html=False, include_plotlyjs=False)
    surf_html = fig_surf.to_html(full_html=False, include_plotlyjs=False)
    traj_html = fig_traj.to_html(full_html=False, include_plotlyjs=False)
    macro_html = fig_macro.to_html(full_html=False, include_plotlyjs=False)

    exercises_html = ""
    for ex in routine["exercises"]:
        exercises_html += f"""
        <div style="background:#21262D; padding:12px; border-radius:6px; margin-bottom:8px; border-left:4px solid #00FF88; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <b style="color:#FFFFFF; font-size:15px;">✓ {ex['name']}</b>
                <div style="color:#8B949E; font-size:13px;">{ex['sets']} sets x {ex['reps']} | Rest: {ex['rest_sec']}s</div>
            </div>
            <span style="background:#00FF88; color:#000000; font-weight:bold; font-size:11px; padding:4px 8px; border-radius:12px;">DONE (100%)</span>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>90-Day Body Recomposition Dashboard</title>
    <style>
        body {{
            background-color: #0D1117;
            color: #C9D1D9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 20px 40px;
        }}
        h1, h2, h3 {{ color: #FFFFFF; margin-top: 0; }}
        .header {{
            background: linear-gradient(135deg, #161B22 0%, #21262D 100%);
            border: 1px solid #30363D;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        }}
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 24px;
        }}
        .grid-3 {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin-bottom: 24px;
        }}
        .card {{
            background: #161B22;
            border: 1px solid #30363D;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        }}
        .badge {{
            display: inline-block;
            background: #238636;
            color: white;
            font-size: 12px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 20px;
            margin-right: 8px;
        }}
        .badge-danger {{
            background: #DA3633;
        }}
    </style>
</head>
<body>
    <div class="header">
        <span class="badge">90-DAY TRANSFORMATION</span>
        <span class="badge" style="background:#8957E5;">PHASE 1: GLUTE & BELLY AWAKENING</span>
        <h1 style="font-size:32px; margin: 10px 0 6px 0;">⚡ DAY {day}: {routine['routine_name']}</h1>
        <p style="color:#8B949E; margin:0; font-size:16px;">Target: Belly Visceral Fat Annihilation & Glute Hypertrophy | Recomp Deficit: -400 kcal</p>
    </div>

    <div class="grid-2">
        <div class="card">
            <h2>🎯 Real-time Completion Gauge</h2>
            {gauge_html}
        </div>
        <div class="card">
            <h2>🥗 Recomposition Diet Target</h2>
            <div style="font-size:14px; margin-bottom:12px;">
                <b>Target Calories:</b> <span style="color:#00FF88;">{macros['target_calories']} kcal</span> | 
                <b>Protein:</b> <span style="color:#00FF88;">{macros['protein_g']}g</span> | 
                <b>Fats:</b> {macros['fat_g']}g | 
                <b>Carbs:</b> {macros['carbs_g']}g | 
                <b>Water:</b> <span style="color:#00F0FF;">{macros['water_liters']}L</span>
            </div>
            {macro_html}
        </div>
    </div>

    <div class="card" style="margin-bottom:24px;">
        <h2>📋 Completed Routine (Day {day})</h2>
        {exercises_html}
    </div>

    <h2>🌐 Interactive 3D Visualizations (100% Beast Mode Unlocked)</h2>
    <div class="grid-3">
        <div class="card">
            {topo_html}
        </div>
        <div class="card">
            {surf_html}
        </div>
        <div class="card">
            {traj_html}
        </div>
    </div>

    <div class="card" style="border-left: 5px solid #FF0055; background: #1C1014;">
        <h2 style="color:#FF0055;">⚡ The Punishment Protocol (Failure Accountability)</h2>
        <p>If daily completion is under 100%, the engine activates the Punishment Ledger:</p>
        <ul>
            <li><b>75% - 99% Completion:</b> Minor Penalty (50 Jump Squats or 3-Minute Continuous Plank)</li>
            <li><b>40% - 74% Completion:</b> Moderate Penalty (60 Chest-to-Floor Burpees + 75 Mountain Climbers)</li>
            <li><b>&lt; 40% Completion:</b> Severe Penalty (100 Burpees, 150 Lunges, 5-Min Ice Cold Shower, 10k Steps Penalty)</li>
        </ul>
    </div>
</body>
</html>
"""

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML Dashboard successfully generated at: {save_path}")

if __name__ == "__main__":
    build_dashboard_html()
