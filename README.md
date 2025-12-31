# Personalized AI Recipe & Meal Planner — PoC

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


