import pandas as pd
import ast
import re
import streamlit as st




def safe_parse(x):
    if isinstance(x, list):
        return " ".join(x)
    if isinstance(x, str):
        try:
            return " ".join(ast.literal_eval(x))
        except:
            return x
    return ""


# import re

def clean_r_list(text):
    if not isinstance(text, str):
        return ""

    text = text.strip()

    # Remove leading c(
    if text.startswith("c("):
        text = text[2:]

    # Remove trailing )
    if text.endswith(")"):
        text = text[:-1]

    # Remove quotes
    text = text.replace('"', '').replace("'", "")

    # Normalize commas and spacing
    parts = [p.strip() for p in text.split(",") if p.strip()]
    return ", ".join(parts)

@st.cache_data(show_spinner="Loading recipes...")
def load_data(path="recipes.csv"):
    df = pd.read_csv(
    path,
    engine="python",
    sep=",",
    quotechar='"',
    on_bad_lines="skip"
)


    df = df[['Name',
             'RecipeIngredientParts',
             'RecipeInstructions',
             'Calories',
             'FatContent',
             'CarbohydrateContent',
             'ProteinContent',
             'FiberContent',
             'SugarContent']]

    df.dropna(inplace=True)

    df['ingredients'] = df['RecipeIngredientParts'].apply(clean_r_list)
    df['instructions'] = df['RecipeInstructions'].apply(clean_r_list)

    
    return df
