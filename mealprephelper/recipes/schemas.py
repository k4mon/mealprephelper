from typing import Set

from pydantic import BaseModel, AnyHttpUrl


class RecipeType(BaseModel):
    name: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"name": "breakfast"}}


class Recipe(BaseModel):
    name: str
    link: AnyHttpUrl
    recipe_types: Set[RecipeType]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Recipe",
                "link": "http://google.com",
                "recipe_types": "breakfast",
            }
        }
