import streamlit as st
import pandas as pd
from ml.data_loader import load_data
from ml.veg_classifier import train_classifier, predict_food_type
from ml.recommender import train_recommender, recommend_recipes
from ml.nutrition import get_nutrition
# from ml.age_profile import get_age_profile
from ml.age_profile import get_age_calorie_limit
from ml.ingredient_semantics import recipe_matches_ingredients



st.set_page_config(
    page_title="Personalized AI Recipe & Meal Planner",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }

    
    div[data-testid="column"] {
        padding: 1.5rem;
        border-radius: 12px;
    }

    
    div[data-testid="column"]:first-child {
        background-color: #1c1f26;   /* dark gray */
    }

    
    div[data-testid="column"]:nth-child(2) {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)


df = load_data(path="recipes.csv")

model, vectorizer = train_classifier(df)
tfidf, tfidf_matrix = train_recommender(df)

left_col, right_col = st.columns([1, 3], gap="large")

with left_col:
    st.markdown("### User Profile")

    age = st.number_input("Age", min_value=10, max_value=100, value=25)

    # gender = st.selectbox(
    #     "Gender",
    #     ["Male", "Female", "Prefer not to say"]
    # )

    diet_type = st.selectbox(
        "Diet type",
        ["No preference", "Vegetarian", "Non-Vegetarian", "Pescatarian", "Keto", "Gluten-Free"]
    )

    daily_calories = st.number_input(
        "Daily calorie goal (kcal)",
        min_value=800,
        max_value=3000,
        value=1650,
        step=100
    )

    ingredients = st.text_input(
        "Ingredients (comma separated)",
        placeholder="tomato, onion, chicken"
    )

    taste_pref = st.text_input(
        "Taste preferences (comma separated, e.g., spicy, savory, sweet)"
    )

    meals_count = st.slider(
        "Meals to generate",
        min_value=1,
        max_value=10,
        value=3
    )

    generate_btn = st.button("Generate Meal Plan")

with right_col:
    st.title("🍽️ The AI Chef")
    st.markdown("## Personalized AI Recipe & Meal Planner")
    st.markdown(""" 
    This application demonstrates how machine learning can recommend recipes  
    based on ingredients, dietary preference, and nutritional constraints.
    """)
    st.divider()
    st.markdown("### Top Recommendations")

    if generate_btn:

    # --------------------------------
    # CASE 1: INGREDIENT-BASED MODE
    # --------------------------------
        if ingredients.strip():

            user_ingredients = [
                i.strip().lower()
                for i in ingredients.split(",")
                if i.strip()
            ]

            recs = df[
                df["ingredients"].apply(
                    lambda x: recipe_matches_ingredients(x, user_ingredients)
                )
            ]

        # --------------------------------
        # CASE 2: DIET + CALORIE MODE
        # --------------------------------
        else:
            recs = df.copy()

        # Age-based calorie recommendation
        age_calorie_limit = get_age_calorie_limit(age)

        # User-defined calorie preference
        user_calorie_limit = daily_calories

        # Final calorie limit (safe + user friendly)
        final_calorie_limit = min(age_calorie_limit, user_calorie_limit)

        # -----------------------------
        # SEMANTIC INGREDIENT FILTER
        # -----------------------------

        # Parse user ingredients (supports one or many)
        user_ingredients = [
            i.strip().lower()
            for i in ingredients.split(",")
            if i.strip()
        ]

        # Filter recipes using real ingredient semantics
        recs = df[
            df["ingredients"].apply(
                lambda x: recipe_matches_ingredients(x, user_ingredients)
            )
        ]


        # ----------------------------
        # Diet Filter
        # ----------------------------
        if diet_type != "No preference":

            if diet_type == "Vegetarian":
                recs = recs[recs["FoodType"] == "Veg"]

            elif diet_type == "Vegan":
                recs = recs[recs["FoodType"] == "Veg"]

            elif diet_type == "Non-Vegetarian":

                meat_keywords = [
                    "chicken", "beef", "mutton", "pork",
                    "lamb", "goat", "turkey", "duck", "egg"
                ]

                fish_keywords = [
                    "fish", "salmon", "tuna", "prawn",
                    "shrimp", "crab", "lobster", "eggplant"
                ]

                recs = recs[
                    recs["ingredients"].apply(
                        lambda x: isinstance(x, str)
                        and any(meat in x.lower() for meat in meat_keywords)
                        and not any(fish in x.lower() for fish in fish_keywords)
                    )
                ]


            elif diet_type == "Pescatarian":

                fish_keywords = [
                    "fish", "salmon", "tuna", "shrimp", "prawn",
                    "crab", "lobster", "cod", "tilapia"
                ]

                meat_keywords = [
                    "chicken", "beef", "mutton", "pork",
                    "lamb", "turkey", "duck", "goat"
                ]

                recs = recs[
                    recs["ingredients"].apply(
                        lambda x: isinstance(x, str)
                        and any(fish in x.lower() for fish in fish_keywords)
                        and not any(meat in x.lower() for meat in meat_keywords)
                    )
                ]



            elif diet_type == "Gluten-Free":

                gluten_keywords = [
                    "wheat", "barley", "rye", "bread",
                    "pasta", "flour", "noodles", "semolina"
                ]

                recs = recs[
                    recs["ingredients"].apply(
                        lambda x: isinstance(x, str)
                        and not any(gluten in x.lower() for gluten in gluten_keywords)
                    )
                ]


            elif diet_type == "Keto":

                high_carb_keywords = [
                    "rice", "bread", "pasta", "potato",
                    "sugar", "flour", "corn", "wheat"
                ]

                recs = recs[
                    (recs["CarbohydrateContent"] <= 20) &   # keto carb limit
                    recs["ingredients"].apply(
                        lambda x: isinstance(x, str)
                        and not any(carb in x.lower() for carb in high_carb_keywords)
                    )
                ]



        # Calorie filter
            recs = recs[recs["Calories"] <= final_calorie_limit]

        st.caption(
            f"Calorie limit applied: {final_calorie_limit} kcal "
            f"(Age-based: {age_calorie_limit} kcal, Your input: {user_calorie_limit} kcal)"
        )

        if recs.empty:
            st.warning("No recipes match your preferences.")
        else:
            for i, (_, row) in enumerate(recs.head(meals_count).iterrows(), 1):
                st.markdown(f"### {i}. {row['Name']}")
                if "Images" in row and isinstance(row["Images"], str) and row["Images"].strip():
                    image_url = row["Images"].split(",")[0].strip()
                    if image_url.startswith("http"):
                        st.image(image_url, use_column_width=True)

                # st.caption("Why this recipe? " + ", ".join(reasons))
                st.caption(f"Cuisine: {row.get('RecipeCategory','N/A')}")

                st.markdown(f"**Calories:** {int(row['Calories'])} kcal")
                st.markdown(
                    f"**Macros (P/C/F):** "
                    f"{int(row['ProteinContent'])}g / "
                    f"{int(row['CarbohydrateContent'])}g / "
                    f"{int(row['FatContent'])}g"
                )

                with st.expander("Ingredients & Directions"):

                # Ingredients label
                    st.markdown("**🧂 Ingredients**")
                    ingredients_list = [i.strip() for i in row["ingredients"].split(",") if i.strip()]
                    for item in ingredients_list:
                        st.markdown(f"- {item}")

                    st.markdown("---")

                    # Directions label
                    st.markdown("**👨‍🍳 Directions**")
                    directions = row["instructions"]

                    # Split directions into steps (best-effort)
                    steps = [
                        s.strip().lstrip(",;- ")
                        for s in directions.split(".")
                        if len(s.strip()) > 5
                    ]

                    for idx, step in enumerate(steps, 1):
                        st.markdown(f"{idx}. {step}")

                    download_text = f"Recipe: {row['Name']}\n\n"
                    
                    if "Images" in row and isinstance(row["Images"], str):
                        image_url = row["Images"].split(",")[0].strip()
                        download_text += f"Image: {image_url}\n\n"


                    download_text += "Ingredients:\n"
                    for ing in ingredients_list:
                        download_text += f"- {ing}\n"

                    download_text += "\nDirections:\n"
                    for idx, step in enumerate(steps, 1):
                        download_text += f"{idx}. {step}\n"

                    st.download_button(
                        label="📥 Download Recipe",
                        data=download_text,
                        file_name=f"{row['Name'].replace(' ', '_')}_recipe.txt",
                        mime="text/plain"
                    )








                            
