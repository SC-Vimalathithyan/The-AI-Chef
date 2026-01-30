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

1. Machine Learning & Logic
2. Ingredient-based filtering (strict matching)
3. Diet-aware recipe generation:
  Vegetarian
  Non-Veg (meat-based only)
  Pescatarian
  Keto (low-carb logic)
  Gluten-Free

4. Derived diet classification from ingredients
5. Age-based + manual calorie constraint
6. Calorie normalization and outlier removal
7. Balanced recommendations for No Preference
8. Explainability: “Why this recipe?”

🎨 Streamlit UI Features

1. Split-view interactive layout
2. Auto-updating results (no refresh needed)
3. Recipe images from dataset (Images column)
4. Expandable ingredients & directions
5. Download recipe instructions as .txt
6. Sliders, dropdowns, and live filters

🏗️ Project Structure
ai-recipe-generator/
│
├── app.py                  
│
├── ml/
│   ├── data_loader.py      
│   ├── recommender.py      c
│
├── recipes.csv         
│
├── requirements.txt
└── README.md

🧪 Dataset Description

The dataset contains:

1. Recipe names
2. Ingredients
3. Cooking instructions
4. Calories
5. Macronutrients (Protein, Carbs, Fat)
6. Food type
7. Recipe images (Images column)

Dataset Challenges Addressed:

1. Inconsistent ingredient formatting
2. Missing diet labels
3. No explicit meat/fish categorization
4. Unrealistic calorie values

All issues are handled through robust preprocessing logic.

🧠 Diet Logic Summary

1. Diet Type	Logic Used
2. Vegetarian	Plant-based only
3. Non-Veg	Meat-based ingredients only
4. Pescatarian	Fish/seafood, no meat
5. Gluten-Free	Excludes gluten ingredients
6. Keto	Low carbs + ingredient filtering
7. No Preference	Balanced mix of all diets

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
1. Download ingredients & directions
2. Includes recipe name and image URL
3. Generated dynamically (no file storage required)

🎓 Academic & Viva Highlights

1. Real-world dataset handling
2. Explainable recommendation logic
3. Diet inference using ingredient heuristics
4. Reactive Streamlit UI
5. Clean separation of ML logic and UI
6. Production-style Proof of Concept (PoC)

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
