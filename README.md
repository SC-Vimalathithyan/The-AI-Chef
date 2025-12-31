🍽️ AI Recipe Generator (Streamlit App)

A machine learning–powered recipe recommendation system built using Python, Scikit-learn, and Streamlit, capable of generating personalized recipes based on dietary preferences, calorie limits, and ingredients.

📌 Project Overview

The AI Recipe Generator is an interactive Streamlit web application that recommends recipes using a real-world recipe dataset.
The system supports both:

Ingredient-based recommendations

Diet + calorie-based recommendations (without ingredients)

The application dynamically updates results as users change inputs and provides recipe images, nutrition details, and downloadable instructions.

🎯 Project Objectives

Build an intelligent recipe recommendation system

Handle real-world dataset inconsistencies

Support multiple dietary preferences

Provide a user-friendly, interactive UI

Demonstrate ML + Streamlit integration

🧠 Key Features
✅ Machine Learning & Logic

Ingredient-based filtering (strict matching)

Diet-aware recipe generation:

Vegetarian

Non-Veg (meat-based only)

Pescatarian

Keto (low-carb logic)

Gluten-Free

Derived diet classification from ingredients

Age-based + manual calorie constraint

Calorie normalization and outlier removal

Balanced recommendations for No Preference

Explainability: “Why this recipe?”

🎨 Streamlit UI Features

Split-view interactive layout

Auto-updating results (no refresh needed)

Recipe images from dataset (Images column)

Expandable ingredients & directions

Download recipe instructions as .txt

Sliders, dropdowns, and live filters# Personalized AI Recipe & Meal Planner — PoC

This repository is a working proof-of-concept for a Personalized AI Recipe & Meal Planner.
It includes a simple Streamlit demo app, a lightweight recommendation engine, sample recipe dataset,
evaluation scripts, and documentation for running a demo/presentation.

## What's included
- `app/streamlit_app.py` — Streamlit UI to interact with the recommender.
- `models/recommender.py` — Simple rule-based + similarity recommender.
- `data/recipes.json` — Small sample recipe dataset with nutrition info.
- `notebooks/` — (Optional) starter notebook for experimentation.
- `requirements.txt` — Python dependencies.
- `demo/` — Demo checklist, narration script and steps for recording.
- `README.md` — (you are reading it)
- `run_demo.sh` — Script to run the Streamlit app locally.

## Quick start (local)
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit demo:
   ```bash
   streamlit run app/streamlit_app.py
   ```
4. Open the URL printed by Streamlit (usually http://localhost:8501).


