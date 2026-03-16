from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter()


@router.post("/", response_model=schemas.FoodItemOut)
def create_food_item(food_item: schemas.FoodItemCreate, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == food_item.restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    new_item = models.FoodItem(**food_item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.get("/", response_model=list[schemas.FoodItemOut])
def get_all_food_items(db: Session = Depends(get_db)):
    return db.query(models.FoodItem).all()


@router.get("/{food_item_id}", response_model=schemas.FoodItemOut)
def get_food_item(food_item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.FoodItem).filter(models.FoodItem.id == food_item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Food item not found")
    return item


@router.delete("/{food_item_id}")
def delete_food_item(food_item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.FoodItem).filter(models.FoodItem.id == food_item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Food item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Food item {food_item_id} deleted"}
