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

Sliders, dropdowns, and live filters

🏗️ Project Structure
ai-recipe-generator/
│
├── app.py                  # Streamlit application
│
├── ml/
│   ├── data_loader.py      # Dataset loading & preprocessing
│   ├── recommender.py      # Recommendation logic
│
├── data/
│   └── recipes.csv         # Recipe dataset
│
├── requirements.txt
└── README.md

🧪 Dataset Description

The dataset contains:

Recipe names

Ingredients

Cooking instructions

Calories

Macronutrients (Protein, Carbs, Fat)

Food type

Recipe images (Images column)

Dataset Challenges Addressed

Inconsistent ingredient formatting

Missing diet labels

No explicit meat/fish categorization

Unrealistic calorie values

All issues are handled through robust preprocessing logic.

🧠 Diet Logic Summary
Diet Type	Logic Used
Vegetarian	Plant-based only
Non-Veg	Meat-based ingredients only
Pescatarian	Fish/seafood, no meat
Gluten-Free	Excludes gluten ingredients
Keto	Low carbs + ingredient filtering
No Preference	Balanced mix of all diets
🚀 How to Run the Streamlit App
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Application
streamlit run app.py

3️⃣ Open in Browser

Streamlit will automatically open at:

http://localhost:8501

🔁 Auto-Update Behavior

Streamlit reruns the app automatically when inputs change

Sliders, dropdowns, and text inputs trigger live updates

Dataset loading is cached for performance

📥 Recipe Download Feature

For each recipe, users can:

Download ingredients & directions

Includes recipe name and image URL

Generated dynamically (no file storage required)

🎓 Academic & Viva Highlights

Real-world dataset handling

Explainable recommendation logic

Diet inference using ingredient heuristics

Reactive Streamlit UI

Clean separation of ML logic and UI

Production-style Proof of Concept (PoC)

🧠 Technologies Used

Python

Pandas, NumPy

Scikit-learn

Streamlit

🔮 Future Enhancements

PDF recipe downloads

Shopping list generation

Favorites system

Cuisine-based filtering

REST API version

Deployment on Streamlit Cloud

👨‍🎓 Project Type

Academic / College Project

Machine Learning Proof of Concept (PoC)

Suitable for:

Machine Learning

Data Science

Streamlit Applications

📜 License

This project is intended for educational purposes only.

⭐ Acknowledgements

Open recipe datasets

Python open-source ecosystem

Streamlit documentation

⭐ If you like this project, consider giving it a star on GitHub!
