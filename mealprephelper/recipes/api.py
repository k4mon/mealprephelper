from typing import List

from fastapi import APIRouter, Depends

from mealprephelper.recipes.factory import create_recipe_service
from mealprephelper.recipes.service.interface import AbstractRecipeService
from mealprephelper.recipes.service.schema import Recipe, RecipeCreate, Ingredient

router = APIRouter()


@router.get("/", response_model=List[Recipe])
def get_recipes(service: AbstractRecipeService = Depends(create_recipe_service)):
    return service.get_recipes()


@router.get("/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int, service: AbstractRecipeService = Depends(create_recipe_service)):
    return service.get_recipe(recipe_id)


@router.post("/", response_model=Recipe)
def create_recipe(
    recipe: RecipeCreate, service: AbstractRecipeService = Depends(create_recipe_service),
):
    return service.create_recipe(recipe)


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(
    recipe_id: int,
    recipe: RecipeCreate,
    service: AbstractRecipeService = Depends(create_recipe_service),
):
    return service.update_recipe(recipe_id, recipe)


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, service: AbstractRecipeService = Depends(create_recipe_service)):
    return service.delete_recipe(recipe_id)


@router.get("/ingredients/", response_model=List[Ingredient])
def get_ingredients(service: AbstractRecipeService = Depends(create_recipe_service)):
    return service.get_ingredients()


@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(
    ingredient_id: int, service: AbstractRecipeService = Depends(create_recipe_service)
):
    return service.delete_ingredient(ingredient_id)
