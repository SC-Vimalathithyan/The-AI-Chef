# Ingredients that indicate processed / derived products
DISALLOWED_DERIVATIVES = {
    "sauce", "stock", "broth", "paste", "powder", "seasoning",
    "cube", "bouillon", "essence", "flavor", "flavour",
    "extract", "mix", "masala", "gravy", "marinade"
}


def normalize(text: str) -> str:
    return text.lower().strip()


def is_real_ingredient(ingredient: str, core: str) -> bool:
    """
    Returns True if `ingredient` represents the real form of `core`
    and not a derived product (sauce, stock, powder, etc.)
    """
    ingredient = normalize(ingredient)
    core = normalize(core)

    # Core must appear as a word
    if core not in ingredient:
        return False

    # Reject derived forms
    for bad in DISALLOWED_DERIVATIVES:
        if bad in ingredient:
            return False

    return True


def recipe_matches_ingredients(recipe_ingredients: str, user_ingredients: list) -> bool:
    """
    Returns True if ALL user ingredients are present as REAL ingredients
    in the recipe.
    """
    recipe_items = [i.strip() for i in recipe_ingredients.split(",")]

    for user_ing in user_ingredients:
        if not any(is_real_ingredient(item, user_ing) for item in recipe_items):
            return False

    return True
