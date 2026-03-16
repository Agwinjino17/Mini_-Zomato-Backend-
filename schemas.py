from pydantic import BaseModel
from typing import Optional


# ─── Customer ───────────────────────────────────────────
class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerOut(CustomerCreate):
    id: int

    class Config:
        orm_mode = True


# ─── Restaurant ─────────────────────────────────────────
class RestaurantCreate(BaseModel):
    name: str
    location: str

class RestaurantOut(RestaurantCreate):
    id: int

    class Config:
        orm_mode = True


# ─── FoodItem ───────────────────────────────────────────
class FoodItemCreate(BaseModel):
    name: str
    price: float
    restaurant_id: int

class FoodItemOut(FoodItemCreate):
    id: int

    class Config:
        orm_mode = True


# ─── Order ──────────────────────────────────────────────
class OrderCreate(BaseModel):
    customer_id: int
    food_item_id: int
    quantity: int

class OrderOut(BaseModel):
    id: int
    customer_id: int
    food_item_id: int
    quantity: int
    total_price: float

    class Config:
        orm_mode = True
