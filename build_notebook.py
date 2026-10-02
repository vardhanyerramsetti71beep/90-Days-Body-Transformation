"""
Builder script to generate the 90_Day_Transformation_Mastery.ipynb notebook
using nbformat for guaranteed syntax and execution stability.
"""

import nbformat as nbf  # type: ignore

nb = nbf.v4.new_notebook()

cells = []

# Cell 1: Markdown Title & Manifesto
cells.append(nbf.v4.new_markdown_cell("""# 🏋️‍♂️ 90-DAY BODY RECOMPOSITION & TRANSFORMATION MASTERY
### **Weight Loss | Muscle Gain | Belly Fat Annihilation | Butt Sculpt & Lift**
---
> **"You don't get the body you wish for; you get the body you work for."**
> 
> Welcome to your comprehensive, scientifically backed **90-Day Transformation Challenge**. This interactive system is engineered to achieve **simultaneous body recomposition**: melting stubborn visceral/subcutaneous belly and hip fat while packing dense, toned muscle on your glutes and core.
>
> 🎯 **What this notebook delivers:**
> 1. **Scientific Recomposition Blueprint**: Calorie deficit calculation, high-protein macro targets, and hormonal optimization.
> 2. **Targeted Belly & Butt Exercise Database**: Biomechanically proven movements to shrink the waistline and lift/round the glutes.
> 3. **Daily Routine (Days 1 to 90)**: Structured 3-phase periodization with progressive overload.
> 4. **Interactive 100% Completion Meter**: Real-time visual gauge tracking your daily execution.
> 5. **3D Visualizations**: Multi-dimensional biomechanical muscle maps, 3D metabolic burn landscapes, and 90-day trajectory paths.
> 6. **The Brutal Punishment Protocol**: Non-negotiable penalty system enforcing accountability if you fail to hit 100%.
"""))

# Cell 2: Code - Imports & Setup
cells.append(nbf.v4.new_code_cell("""# Environment Setup & Core Engine Import
import sys
import os
import json
import random
from datetime import datetime
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import plotly.graph_objects as go  # type: ignore
import plotly.express as px  # type: ignore
from plotly.subplots import make_subplots  # type: ignore
from IPython.display import display, clear_output  # type: ignore
from IPython.core.display import HTML  # type: ignore
import ipywidgets as widgets  # type: ignore

# Import local fitness engine
import fitness_engine as fe

# Initialize progress store
progress_data = fe.load_progress()
print("🔥 Transformation Engine Initialized Successfully!")
print(f"Current Challenge Day: Day {progress_data.get('current_day', 1)} / 90")
"""))

# Cell 3: Markdown - Diet & Nutrition Section
cells.append(nbf.v4.new_markdown_cell(r"""## 🥗 SECTION 1: PROPER DIET & NUTRITION ARCHITECTURE
---
### The Golden Rule of Body Recomposition
To **lose belly fat** while simultaneously **building and firming the butt**, you must operate in a **controlled caloric deficit (300–400 kcal below TDEE)** combined with **high protein (1.8 – 2.2g per kg bodyweight)**:
* **Why high protein?** Protein has a high thermic effect ($20\text{-}30\%$ of calories burned just digesting it) and provides amino acids to synthesize new glute and core muscle fibers even while in a deficit.
* **Why low-GI carbs?** Keeps insulin low throughout the day, unlocking visceral and abdominal adipose fat stores for fuel.
* **Why 4 liters of water?** Electrolyte balance eliminates water retention under the skin that creates a false "belly bloat".

Run the cell below to compute your custom macros and review the meal plan.
"""))

# Cell 4: Code - Macro Calculator & Interactive Meal Plan
cells.append(nbf.v4.new_code_cell("""# 1. Custom Nutrition & Macro Calculator
# Enter your current physical stats below:
USER_WEIGHT_KG = 74.0     # Your current bodyweight (kg)
USER_HEIGHT_CM = 175.0    # Your height (cm)
USER_AGE = 25             # Your age
USER_GENDER = "male"      # "male" or "female"
USER_ACTIVITY = "moderate"# "sedentary", "light", "moderate", "very_active"

macros = fe.NutritionEngine.calculate_macros(
    weight_kg=USER_WEIGHT_KG,
    height_cm=USER_HEIGHT_CM,
    age=USER_AGE,
    gender=USER_GENDER,
    activity_level=USER_ACTIVITY
)

# Display Macro Summary
print("==========================================================")
print(f"🔥 YOUR PERSONALIZED 90-DAY RECOMPOSITION MACROS:")
print(f"   • Maintenance TDEE:      {macros['tdee']} kcal/day")
print(f"   • Target Fat-Loss Intake: {macros['target_calories']} kcal/day (-400 kcal Deficit)")
print(f"   • Daily Protein Target:   {macros['protein_g']}g ({round(macros['protein_g']*4/macros['target_calories']*100)}% of diet)")
print(f"   • Daily Healthy Fats:     {macros['fat_g']}g ({round(macros['fat_g']*9/macros['target_calories']*100)}% of diet)")
print(f"   • Daily Complex Carbs:    {macros['carbs_g']}g ({round(macros['carbs_g']*4/macros['target_calories']*100)}% of diet)")
print(f"   • Daily Water Intake:     {macros['water_liters']} Liters (Non-negotiable)")
print("==========================================================")

# Plot Macro Pie Donut
fig_macros = go.Figure(data=[go.Pie(
    labels=['Protein (Muscle Growth)', 'Healthy Fats (Hormones)', 'Complex Carbs (Energy)'],
    values=[macros['protein_g']*4, macros['fat_g']*9, macros['carbs_g']*4],
    hole=.45,
    marker_colors=['#00FF88', '#FFB800', '#00B4D8']
)])
fig_macros.update_layout(
    title_text="<b>DAILY CALORIE SPLIT (BODY RECOMPOSITION)</b>",
    template="plotly_dark",
    height=350,
    margin=dict(l=20, r=20, t=50, b=20)
)
fig_macros.show()
"""))

# Cell 5: Code - Anti-Belly Fat Meal Plan Viewer
cells.append(nbf.v4.new_code_cell("""# 2. Daily Anti-Belly Fat & Glute-Fuel Meal Blueprint
meal_plan = fe.NutritionEngine.get_meal_plan()

for meal_title, details in meal_plan.items():
    print(f"\\n🔹 {meal_title.upper()}")
    if isinstance(details, dict):
        for k, v in details.items():
            print(f"   [{k}]: {v}")
    else:
        print(f"   {details}")
"""))

# Cell 6: Markdown - Targeted Exercises Breakdown
cells.append(nbf.v4.new_markdown_cell("""## 🍑 & ⚡ SECTION 2: TARGETED BELLY FAT & BUTT SCULPT EXERCISES
---
### Why Spot Reduction is a Myth, BUT Localized Sculpting is 100% Real:
While fat is mobilized systemically across your entire body through a caloric deficit, **you can dramatically sculpt, tighten, and shape specific regions**:
1. **Butt Fat Reduction & Glute Hypertrophy**:
   - The gluteus maximus is the largest muscle in the human body. When you load it with progressive resistance (Hip Thrusts, Bulgarian Split Squats, RDLs), muscle fibers hypertrophy, pushing up against the subcutaneous fat layer, pulling it tight and creating a lifted, round, aesthetic shape.
2. **Belly Fat Annihilation & Waist Taper**:
   - Direct ab work (Hanging Leg Raises, Woodchoppers, Ab Wheel) hypertrophies the abdominal wall so deep lines ("six pack") show as body fat drops.
   - **Transverse Abdominis (TVA) Vacuum Holds**: Acts as the body's natural inner corset. By training TVA isometric holds, your resting waistline physically pulls inward by 2–3 inches.
   - **High-Intensity Intervals (HIIT / Kettlebell Swings)**: Triggers intense catecholamine (epinephrine/norepinephrine) release that specifically binds to alpha-2 receptors in stubborn visceral and lower belly fat.
"""))

# Cell 7: Code - Exercise Database Inspector
cells.append(nbf.v4.new_code_cell("""# Targeted Exercise Inspector
import pandas as pd  # type: ignore
from IPython.display import display  # type: ignore
from IPython.core.display import HTML  # type: ignore
import fitness_engine as fe

ex_df = pd.DataFrame([
    {
        "Exercise": name,
        "Target Area": data["target_area"],
        "Muscle": data["muscle"],
        "Exercise Type": data["type"],
        "Burn (Cal/min)": data["cals_per_min"],
        "Joint Kinematics": data.get("joint_focus", "Spine neutral, full ROM"),
        "Tempo Cadence": data.get("tempo", "3-1-1-0"),
        "Biomechanical Animation": f'⚡ Animation: <b>{data.get("animation_id", "routine")}</b>'
    }
    for name, data in fe.EXERCISE_DATABASE.items()
])

# Filter specifically for Belly and Butt
belly_butt_df = ex_df[ex_df["Target Area"].str.contains("Belly|Butt", case=False)]
display(HTML(belly_butt_df.to_html(classes="table table-dark table-striped", escape=False, index=False)))
"""))

# Cell 8: Markdown - Interactive Daily Workout Tracker & 100% Completion Meter
cells.append(nbf.v4.new_markdown_cell("""## 📊 SECTION 3: DAILY WORKOUT EXECUTION & 100% COMPLETION METER
---
Select any day from **Day 1 to 90** below. Check off each exercise as you perform your sets.
* As you complete each movement, the **100% Completion Gauge** updates live.
* **If you hit 100%**: The gauge glows neon green and automatically unlocks the **3D Biomechanical & Metabolic Visualizer**!
* **If you fail to reach 100%**: The **Punishment Engine** instantly activates and charges you a penalty debt!
"""))

# Cell 9: Code - Interactive Workout Logger & Live Gauge
cells.append(nbf.v4.new_code_cell("""# Interactive Daily Workout Logger & Completion Meter
import ipywidgets as widgets  # type: ignore
from IPython.display import display, clear_output  # type: ignore
from IPython.core.display import HTML  # type: ignore
import fitness_engine as fe

class WorkoutTrackerUI:
    def __init__(self):
        self.progress = fe.load_progress()
        self.current_day = self.progress.get("current_day", 1)
        
        # Day selector slider
        self.day_slider = widgets.IntSlider(
            value=self.current_day,
            min=1,
            max=90,
            step=1,
            description='Select Day:',
            continuous_update=False,
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='450px')
        )
        self.day_slider.observe(self.on_day_change, names='value')
        
        # Exercise checkboxes container
        self.checkboxes = []
        self.checkbox_container = widgets.VBox()
        
        # Submit Button
        self.submit_btn = widgets.Button(
            description='SUBMIT WORKOUT STATUS',
            button_style='success',
            tooltip='Submit your workout to evaluate completion meter or trigger punishment',
            icon='check-circle',
            layout=widgets.Layout(width='320px', height='45px')
        )
        self.submit_btn.on_click(self.on_submit)
        
        # Output zones
        self.gauge_output = widgets.Output()
        self.result_output = widgets.Output()
        self.viz_output = widgets.Output()
        
        self.render_day(self.current_day)
        
    def render_day(self, day_num):
        routine_info = fe.get_day_routine(day_num)
        self.checkboxes = []
        cb_list = []
        
        header_html = widgets.HTML(f\"\"\"
        <div style="background-color:#161B22; padding:15px; border-radius:8px; border-left:5px solid #00FF88; margin-bottom:12px;">
            <h3 style="color:#FFFFFF; margin:0;">🔥 DAY {day_num}: {routine_info['routine_name']}</h3>
            <p style="color:#00FF88; margin:4px 0 0 0; font-weight:bold;">{routine_info['phase_title']}</p>
            <p style="color:#AAAAAA; margin:4px 0 0 0;"><i>Focus: {routine_info['focus']}</i></p>
        </div>
        \"\"\")
        cb_list.append(header_html)
        
        # Previously completed set
        completed_set = set(self.progress.get("completed_workouts", {}).get(str(day_num), []))
        
        for ex in routine_info["exercises"]:
            name = ex["name"]
            is_checked = name in completed_set
            cb = widgets.Checkbox(
                value=is_checked,
                description=f"{name} — [{ex['sets']} sets x {ex['reps']}] (Rest: {ex['rest_sec']}s)",
                disabled=False,
                indent=False,
                layout=widgets.Layout(width='95%')
            )
            self.checkboxes.append((name, cb))
            cb_list.append(cb)
            
        self.checkbox_container.children = tuple(cb_list)
        self.update_gauge(day_num)
        
    def on_day_change(self, change):
        day_num = change['new']
        self.render_day(day_num)
        with self.result_output:
            clear_output()
        with self.viz_output:
            clear_output()
            
    def update_gauge(self, day_num):
        checked = [name for name, cb in self.checkboxes if cb.value]
        total = len(self.checkboxes)
        fig_gauge, pct, is_comp = fe.create_completion_meter(len(checked), total, day_num)
        
        with self.gauge_output:
            clear_output(wait=True)
            display(fig_gauge)
            
    def on_submit(self, b):
        day_num = self.day_slider.value
        checked = [name for name, cb in self.checkboxes if cb.value]
        total = len(self.checkboxes)
        
        self.update_gauge(day_num)
        
        # Save progress
        if "completed_workouts" not in self.progress:
            self.progress["completed_workouts"] = {}
        self.progress["completed_workouts"][str(day_num)] = checked
        fe.save_progress(self.progress)
        
        eval_result = fe.PunishmentManager.evaluate_workout(len(checked), total, day_num)
        
        with self.result_output:
            clear_output()
            if not eval_result["punished"]:
                display(HTML(f\"\"\"
                <div style="background-color:#0A2F1D; border:2px solid #00FF88; border-radius:10px; padding:20px; margin-top:15px;">
                    <h2 style="color:#00FF88; margin:0;">🏆 100% WORKOUT COMPLETE — BEAST MODE UNLOCKED!</h2>
                    <p style="color:#FFFFFF; font-size:16px;">Exceptional discipline on Day {day_num}. You hit 100% of all required sets and reps!</p>
                    <p style="color:#AAAAAA;">Zero penalty owed. 3D Biomechanical & Kinetic graphs are generated below.</p>
                </div>
                \"\"\"))
            else:
                pun = eval_result["punishment"]
                # Save to punishment ledger
                self.progress["punishment_ledger"].append(eval_result["debt_record"])
                fe.save_progress(self.progress)
                
                display(HTML(f\"\"\"
                <div style="background-color:#360812; border:2px solid #FF0055; border-radius:10px; padding:20px; margin-top:15px;">
                    <h2 style="color:#FF0055; margin:0;">🚨 WORKOUT INCOMPLETE! {eval_result['pct']:.0f}% COMPLETION DETECTED</h2>
                    <h4 style="color:#FFB800; margin:5px 0;">{eval_result['tier_label']}</h4>
                    <div style="background-color:#1A0005; padding:15px; border-radius:8px; border-left:4px solid #FF0055; margin-top:10px;">
                        <h3 style="color:#FFFFFF; margin:0;">💥 ASSIGNED PUNISHMENT: {pun['title']}</h3>
                        <p style="color:#FFD60A; font-size:18px; font-weight:bold; margin:6px 0;">Task: {pun['reps']}</p>
                        <p style="color:#CCCCCC; margin:2px 0;">Debt Impact: {pun['cardio_debt']}</p>
                    </div>
                    <p style="color:#FF8888; font-size:14px; margin-top:12px;">⚠️ <i>This failure has been recorded in your permanent Debt Ledger. You must pay it off before day streak resets!</i></p>
                </div>
                \"\"\"))
                
        # Generate 3D Graphs
        with self.viz_output:
            clear_output()
            print("Rendering 3D Interactive Analytics...")
            g1 = fe.generate_3d_muscle_topology(checked, day_num)
            display(g1)
            g2 = fe.generate_3d_performance_surface(checked, day_num)
            display(g2)
            g3 = fe.generate_3d_90day_trajectory(day_num)
            display(g3)

# Instantiate Tracker
tracker = WorkoutTrackerUI()
display(tracker.day_slider)
display(tracker.checkbox_container)
display(tracker.submit_btn)
display(tracker.gauge_output)
display(tracker.result_output)
display(tracker.viz_output)
"""))

# Cell 10: Markdown - Section 4: 3D Visualization Deep Dive
cells.append(nbf.v4.new_markdown_cell("""## 🌐 SECTION 4: 3D VISUALIZATION DEEP DIVE
---
### Understanding Your 3D Graphs:
1. **3D Biomechanical & Muscle Topology Map**:
   - Represents the human body as a 3D kinetic coordinate frame.
   - Shows real-time hypertrophy and metabolic activation nodes on the **Gluteus Maximus/Medius (Butt)** and the **Rectus & Transverse Abdominis (Belly)**.
   - Dashed neon lines visualize the kinetic chain linking deep core stability with posterior chain power.
2. **3D Metabolic Burn & Fat Oxidation Surface**:
   - A continuous 3D mathematical landscape displaying how time-under-tension and exercise intensity compound to burn calories and induce EPOC (Excess Post-Exercise Oxygen Consumption).
3. **3D 90-Day Transformation Manifold**:
   - A spatial trajectory mapping your 90-day pathway from starting body fat % to your goal physique while muscle mass increases.
"""))

# Cell 11: Markdown - Section 5: The Brutal Punishment Engine
cells.append(nbf.v4.new_markdown_cell("""## ⚡ SECTION 5: THE BRUTAL PUNISHMENT PROTOCOL
---
### The Accountability Law:
If you miss a workout or quit halfway, **you accumulate physical debt**. There are NO free passes. 
The Punishment Engine records all infractions in your permanent ledger:

| Completion % | Severity Tier | Example Penalties |
| :--- | :--- | :--- |
| **75% – 99%** | **Level 1: Minor Infraction** | 50 Jump Squats or 3-Minute Continuous Plank |
| **40% – 74%** | **Level 2: Complacency Offense** | 60 Full Burpees + 75 Mountain Climbers + 5,000 steps penalty |
| **< 40% or Skipped** | **Level 3: Total Surrender** | 100 Burpees + 150 Walking Lunges + 5-min Ice Shower + No Sugar for 7 Days |

Execute the cell below to inspect your outstanding debt ledger and clear paid punishments!
"""))

# Cell 12: Code - Punishment Ledger & Debt Resolver UI
cells.append(nbf.v4.new_code_cell("""# Punishment Ledger & Debt Resolver
import random
import pandas as pd  # type: ignore
import ipywidgets as widgets  # type: ignore
from IPython.display import display, clear_output  # type: ignore
from IPython.core.display import HTML  # type: ignore
import fitness_engine as fe

def show_punishment_ledger():
    prog = fe.load_progress()
    ledger = prog.get("punishment_ledger", [])
    
    if not ledger:
        display(HTML(\"\"\"
        <div style="background-color:#0D2818; padding:15px; border-radius:8px; border-left:5px solid #00FF88;">
            <h3 style="color:#00FF88; margin:0;">✨ CLEAN RECORD: ZERO OUTSTANDING PUNISHMENT DEBT!</h3>
            <p style="color:#DDDDDD; margin:4px 0 0 0;">You have never failed a workout. Keep this pristine streak alive!</p>
        </div>
        \"\"\"))
        return
        
    print(f"Total Infractions Recorded: {len(ledger)}")
    df_ledger = pd.DataFrame(ledger)
    display(df_ledger[["day", "completed_pct", "tier", "punishment_title", "punishment_task", "paid"]])

show_punishment_ledger()

# Interactive Random Punishment Wheel (For Testing or Extra Discipline Challenge)
def spin_punishment_wheel(b):
    tiers = ["minor", "moderate", "severe"]
    tier = random.choice(tiers)
    pun = random.choice(fe.PUNISHMENT_TIERS[tier])
    with punish_output:
        clear_output()
        display(HTML(f\"\"\"
        <div style="background-color:#2A000A; border:2px solid #FF0055; padding:15px; border-radius:8px;">
            <h3 style="color:#FF0055; margin:0;">🎡 ROULETTE PUNISHMENT DRAWN: {pun['title']}</h3>
            <p style="color:#FFFFFF; font-size:16px; margin:5px 0;"><b>Penalty:</b> {pun['reps']}</p>
            <p style="color:#FFB800; margin:2px 0;">Severity: {pun['severity']} | {pun['cardio_debt']}</p>
        </div>
        \"\"\"))

wheel_btn = widgets.Button(
    description='SPIN PUNISHMENT WHEEL',
    button_style='danger',
    icon='bolt',
    layout=widgets.Layout(width='280px', height='40px')
)
wheel_btn.on_click(spin_punishment_wheel)
punish_output = widgets.Output()

display(wheel_btn)
display(punish_output)
"""))

# Cell 13: Markdown - Section 6: 90-Day Weekly Measurement Tracker
cells.append(nbf.v4.new_markdown_cell("""## 📏 SECTION 6: 90-DAY MEASUREMENT & RECOMPOSITION TRACKER
---
Track your physical transformation every 7 days:
* **Waist Circumference (cm)**: Primary indicator of belly fat reduction.
* **Hip & Glute Circumference (cm)**: Metric for butt toning and glute hypertrophy.
* **Bodyweight (kg)**: Track overall scale progress.
"""))

# Cell 14: Code - Weekly Measurement Logger & Chart
cells.append(nbf.v4.new_code_cell("""# Log Weekly Measurement
from datetime import datetime
import numpy as np  # type: ignore
import plotly.graph_objects as go  # type: ignore
from plotly.subplots import make_subplots  # type: ignore
import fitness_engine as fe

def log_measurement(day: int, weight: float, waist: float, hips: float):
    prog = fe.load_progress()
    record = {
        "day": day,
        "weight_kg": weight,
        "waist_cm": waist,
        "hips_cm": hips,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    prog.setdefault("weight_history", []).append(record)
    fe.save_progress(prog)
    print(f"✅ Day {day} measurement saved! Waist: {waist}cm | Hips/Glutes: {hips}cm | Weight: {weight}kg")

# Simulated 90-Day Progression Visualization (What your trajectory will look like)
demo_days = np.array([1, 14, 28, 42, 56, 70, 84, 90])
demo_weight = np.array([78.0, 76.8, 75.5, 74.3, 73.2, 72.4, 71.5, 71.0])
demo_waist = np.array([92.0, 89.5, 87.0, 84.5, 82.0, 80.0, 78.5, 77.0])  # Belly fat melting (-15cm)
demo_hips = np.array([96.0, 96.5, 97.2, 98.0, 98.8, 99.5, 100.2, 100.5]) # Butt muscle growing (+4.5cm)

fig_track = make_subplots(specs=[[{"secondary_y": True}]])
fig_track.add_trace(
    go.Scatter(x=demo_days, y=demo_waist, name="Waist Circumference (Belly Fat Loss)", line=dict(color="#00F0FF", width=3)),
    secondary_y=False
)
fig_track.add_trace(
    go.Scatter(x=demo_days, y=demo_hips, name="Hip/Glute Circumference (Butt Sculpt)", line=dict(color="#FF007F", width=3)),
    secondary_y=False
)
fig_track.add_trace(
    go.Scatter(x=demo_days, y=demo_weight, name="Body Weight (kg)", line=dict(color="#FFB800", width=2, dash="dot")),
    secondary_y=True
)

fig_track.update_layout(
    title_text="<b>90-DAY TRANSFORMATION: WAIST SHRINKING VS GLUTE HYPERTROPHY</b>",
    template="plotly_dark",
    height=450
)
fig_track.update_xaxes(title_text="Day of Challenge")
fig_track.update_yaxes(title_text="Circumference (cm)", secondary_y=False)
fig_track.update_yaxes(title_text="Weight (kg)", secondary_y=True)
fig_track.show()
"""))

# Cell 15: Markdown - Final Words & Daily Oath
cells.append(nbf.v4.new_markdown_cell("""## 🗡️ THE 90-DAY WARRIOR OATH
---
> 1. **No skipped days**: If life gets busy, active recovery or a compressed session is performed.
> 2. **No hidden calories**: Log meals honestly; respect the -400 kcal recomp deficit.
> 3. **Honor the penalty**: If a workout falls short of 100%, pay your physical debt immediately without hesitation.
> 4. **Sleep & hydrate**: 4 liters of water and 8 hours of sleep are as important as the heaviest squat.
>
> **Day 1 begins today. Open the controls in Section 3, crush your exercises, and unlock the 100% Beast Mode Meter!**
"""))

nb['cells'] = cells

output_path = "d:/PROJECTS/90-day-body-transformation/90_Day_Transformation_Mastery.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Successfully generated master notebook at: {output_path}")
