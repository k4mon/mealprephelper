from typing import List

from pydantic import BaseModel, AnyHttpUrl


class RecipeTypeBase(BaseModel):
    name: str
    color: str


class RecipeType(RecipeTypeBase):
    id: int


class IngredientBase(BaseModel):
    name: str


class Ingredient(IngredientBase):
    id: int


class RecipeIngredient(IngredientBase):
    amount: str
    unit: str


class RecipeBase(BaseModel):
    name: str
    link: AnyHttpUrl


class RecipeCreate(RecipeBase):
    recipe_types: List[str]
    ingredients: List[RecipeIngredient]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Recipe",
                "link": "http://google.com",
                "recipe_types": ["breakfast"],
            }
        }


class Recipe(RecipeBase):
    id: int
    recipe_types: List[RecipeType]
    ingredients: List[RecipeIngredient]
