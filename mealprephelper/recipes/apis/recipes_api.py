from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mealprephelper.database.database import get_db
from mealprephelper.recipes import schemas as recipe_schema, service as recipe_service

router = APIRouter()


@router.get("/", response_model=List[recipe_schema.Recipe])
def get_recipes(db: Session = Depends(get_db)):
    return recipe_service.get_recipes(db)


@router.get("/{recipe_id}", response_model=recipe_schema.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_service.get_recipe(db, recipe_id)


@router.post("/", response_model=recipe_schema.Recipe)
def create_recipe(
    recipe: recipe_schema.RecipeCreate, db: Session = Depends(get_db),
):
    return recipe_service.create_recipe(db, recipe)


@router.put("/{recipe_id}", response_model=recipe_schema.Recipe)
def update_recipe(
    recipe_id: int, recipe: recipe_schema.RecipeCreate, db: Session = Depends(get_db),
):
    return recipe_service.update_recipe(db, recipe_id, recipe)


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_service.delete_recipe(db, recipe_id)
