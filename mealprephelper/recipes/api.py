from typing import List

from fastapi import APIRouter, Depends

from mealprephelper.config import oauth2_scheme
from mealprephelper.recipes.factory import create_recipe_service
from mealprephelper.recipes.schema import Recipe, RecipeCreate, Ingredient, RecipeType
from mealprephelper.recipes.service.interface import AbstractRecipeService
from mealprephelper.token import get_username_from_token

router = APIRouter()


@router.get("/", response_model=List[Recipe])
def get_recipes(
    service: AbstractRecipeService = Depends(create_recipe_service),
    token: str = Depends(oauth2_scheme),
):
    return service.get_recipes(get_username_from_token(token))


@router.get("/{recipe_id}", response_model=Recipe)
def get_recipe(
    recipe_id: int,
    service: AbstractRecipeService = Depends(create_recipe_service),
    token=Depends(oauth2_scheme),
):
    return service.get_recipe(get_username_from_token(token), recipe_id)


@router.post("/", response_model=Recipe)
def create_recipe(
    recipe: RecipeCreate,
    service: AbstractRecipeService = Depends(create_recipe_service),
    token=Depends(oauth2_scheme),
):
    return service.create_recipe(get_username_from_token(token), recipe)


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(
    recipe_id: int,
    recipe: RecipeCreate,
    service: AbstractRecipeService = Depends(create_recipe_service),
    token=Depends(oauth2_scheme),
):
    return service.update_recipe(get_username_from_token(token), recipe_id, recipe)


@router.delete("/{recipe_id}")
def delete_recipe(
    recipe_id: int,
    service: AbstractRecipeService = Depends(create_recipe_service),
    token=Depends(oauth2_scheme),
):
    return service.delete_recipe(get_username_from_token(token), recipe_id)


@router.get("/recipe_types/", response_model=List[RecipeType])
def get_recipe_types(
    service: AbstractRecipeService = Depends(create_recipe_service), token=Depends(oauth2_scheme)
):
    return service.get_recipe_types(get_username_from_token(token))


@router.get("/ingredients/", response_model=List[Ingredient])
def get_ingredients(
    service: AbstractRecipeService = Depends(create_recipe_service), token=Depends(oauth2_scheme)
):
    get_username_from_token(token)
    return service.get_ingredients()


@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(
    ingredient_id: int,
    service: AbstractRecipeService = Depends(create_recipe_service),
    token=Depends(oauth2_scheme),
):
    get_username_from_token(token)
    return service.delete_ingredient(ingredient_id)
