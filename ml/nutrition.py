def get_nutrition(recipe_row):
    return {
        "Calories": recipe_row['Calories'],
        "Protein": recipe_row['ProteinContent'],
        "Carbs": recipe_row['CarbohydrateContent'],
        "Fat": recipe_row['FatContent'],
        "Fiber": recipe_row['FiberContent'],
        "Sugar": recipe_row['SugarContent']
    }
