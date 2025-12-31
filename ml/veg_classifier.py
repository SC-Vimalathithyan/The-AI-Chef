from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

NON_VEG_WORDS = [
    'chicken','fish','beef','pork','mutton',
    'lamb','egg','shrimp','bacon','turkey'
]

def label_food_type(ingredients):
    return 'Non-Veg' if any(w in ingredients for w in NON_VEG_WORDS) else 'Veg'

def train_classifier(df):
    df['FoodType'] = df['ingredients'].apply(label_food_type)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['ingredients'])
    y = df['FoodType']

    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer

def predict_food_type(model, vectorizer, user_input):
    vec = vectorizer.transform([user_input])
    return model.predict(vec)[0]
