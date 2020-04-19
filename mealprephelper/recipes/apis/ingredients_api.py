from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mealprephelper.database.database import get_db
from mealprephelper.recipes import schemas as ingredient_schema, service as ingredient_service

router = APIRouter()


@router.get("/", response_model=List[ingredient_schema.Ingredient])
def get_ingredients(db: Session = Depends(get_db)):
    return ingredient_service.get_ingredients(db)


@router.get("/{recipe_id}", response_model=ingredient_schema.Ingredient)
def get_ingredient(recipe_id: int, db: Session = Depends(get_db)):
    return ingredient_service.get_ingredient(db, recipe_id)


@router.post("/", response_model=ingredient_schema.Ingredient)
def create_ingredient(
    recipe: ingredient_schema.IngredientBase, db: Session = Depends(get_db),
):
    return ingredient_service.create_ingredient(db, recipe)


@router.delete("/{recipe_id}")
def delete_ingredient(recipe_id: int, db: Session = Depends(get_db)):
    return ingredient_service.delete_ingredient(db, recipe_id)
