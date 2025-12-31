# Demo Instructions & Narration Script

This document guides you through recording a 3-5 minute demo video for your presentation.

## Environment setup (before recording)
1. Create and activate a Python virtual environment.
2. Install requirements: `pip install -r requirements.txt`.
3. Run the app: `streamlit run app/streamlit_app.py`.
4. Open the app in your browser (http://localhost:8501).

## Demo flow (suggested ~3-5 minutes)
- 0:00–0:20 — Start: Slide title and brief one-line pitch.
- 0:20–0:40 — Introduce user profile in sidebar (diet, allergies, calorie goal).
- 0:40–1:40 — Generate top 3 meal recommendations, open first recipe details, show nutrition panel.
- 1:40–2:20 — Add recipes to grocery list, download list, explain how grocery mapping would work.
- 2:20–3:00 — Change dietary preference (e.g., Vegan), show updated recommendations.
- 3:00–3:30 — Conclude: mention next steps (ML personalization, API integration, productionization).

## Narration sample
"This is a prototype of our Personalized AI Meal Planner. On the left I enter a user profile including dietary preferences and calorie goals. The system filters recipes, ranks them to match the user's goals, and displays nutritional information so users can pick balanced meals. We can add items to a grocery list and export it for shopping. For the prototype we demonstrate core functionality: personalization, nutrition checking, and grocery generation — next steps include training a model on larger datasets and adding continuous learning from feedback."

## Recording tips
- Use OBS Studio or QuickTime to record your screen.
- Record the browser window with the Streamlit app, set microphone for narration.
- Use the script above; keep it natural and concise.
