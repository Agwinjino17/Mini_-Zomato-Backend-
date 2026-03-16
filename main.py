from fastapi import FastAPI
from database import engine, Base
from routers import customers, restaurants, food_items, orders

# Auto-create all tables in PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini Zomato 🍕",
    description="Food Delivery API built with FastAPI + PostgreSQL",
    version="1.0.0"
)

app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(food_items.router, prefix="/food-items", tags=["Food Items"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


@app.get("/")
def root():
    return {"message": "Welcome to Mini Zomato API 🍕"}
