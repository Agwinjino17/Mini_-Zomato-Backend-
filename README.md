# Mini Zomato 🍕 - FastAPI + PostgreSQL

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. PostgreSQL Setup
```bash
# PostgreSQL la login panni database create pannu
createdb mini_zomato

# database.py la ungal password update pannu
# DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/mini_zomato"
```

### 3. Run the server
```bash
uvicorn main:app --reload
```

### 4. Swagger UI
Open browser → http://localhost:8000/docs

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /customers/ | Create customer |
| GET | /customers/ | Get all customers |
| GET | /customers/{id} | Get customer by ID |
| DELETE | /customers/{id} | Delete customer |
| POST | /restaurants/ | Create restaurant |
| GET | /restaurants/ | Get all restaurants |
| POST | /food-items/ | Add food item |
| GET | /food-items/ | Get all food items |
| POST | /orders/ | Place order (auto calculates total) |
| GET | /orders/ | Get all orders |
| DELETE | /orders/{id} | Cancel order |

---

## Project Structure
```
mini_zomato/
├── main.py          → FastAPI app entry point
├── database.py      → PostgreSQL connection
├── models.py        → SQLAlchemy ORM models (DB Tables)
├── schemas.py       → Pydantic schemas (Request/Response)
├── requirements.txt → Dependencies
└── routers/
    ├── customers.py
    ├── restaurants.py
    ├── food_items.py
    └── orders.py
```
