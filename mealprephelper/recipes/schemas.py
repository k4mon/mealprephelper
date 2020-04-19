from typing import List

from pydantic import BaseModel, AnyHttpUrl


class RecipeType(BaseModel):
    id: int
    name: str
    color: str

    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    name: str
    link: AnyHttpUrl


class RecipeCreate(RecipeBase):
    recipe_types: List[str]

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
    name: str
    link: AnyHttpUrl
    recipe_types: List[RecipeType]

    class Config:
        orm_mode = True