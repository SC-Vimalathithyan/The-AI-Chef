# The-AI-Chef
People and industries lack intelligent, personalized solutions for cooking, creative work, and innovation. Key issues include poor recipe personalization, no ingredient/nutrition support, limited AI collaboration, weak content verification, and slow, data-heavy drug discovery. 

This project is a full-stack MVP for an AI-powered recipe generator. It allows users to input ingredients, apply dietary filters, and receive personalized recipes with nutrition info.

📦 Project Structure

recipe-app/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── gpt_engine.py
│   │   ├── nutrition.py
│   │   └── utils.py
│   ├── tests/
│   │   └── test_recipe.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── IngredientInput.jsx
│   │   │   ├── RecipeCard.jsx
│   │   │   └── FilterPanel.jsx
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
└── README.md

🚀 Getting Started

Prerequisites

Python 3.11

Node.js 18+

Docker (optional)

Backend Setup

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend Setup

cd frontend
npm install
npm start

🐳 Docker Setup

Build and Run

docker-compose up --build

Access frontend at http://localhost:3000 and backend at http://localhost:8000.

🧪 Testing

Backend Unit Tests

cd backend
pytest

🧪 Simulated User Flow

User enters ingredients: chickpeas, onion, garlic

Selects filters: Vegetarian, avoids nuts

Clicks "Generate Recipe"

Backend returns recipe with nutrition info

Frontend displays recipe card

📤 Deployment

Render (Backend)

Connect GitHub repo

Build command: pip install -r requirements.txt

Start command: uvicorn app.main:app --host 0.0.0.0 --port 8000

Vercel (Frontend)

Connect GitHub repo

Auto-detect React

Set environment variable for backend URL

📬 Feedback

We welcome feedback from users and contributors!

Report issues

Suggest features

Submit pull requests

📄 License

MIT License — feel free to use and modify.

🙌 Acknowledgments

Thanks to OpenAI, Edamam, Spoonacular, and the open-source community for inspiration and tools.
