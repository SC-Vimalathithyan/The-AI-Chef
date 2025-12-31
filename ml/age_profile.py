def get_age_calorie_limit(age):
    if age <= 12:
        return 1600
    elif age <= 18:
        return 2000
    elif age <= 30:
        return 2400
    elif age <= 45:
        return 2200
    elif age <= 60:
        return 2000
    else:
        return 1800
