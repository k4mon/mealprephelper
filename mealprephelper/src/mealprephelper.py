import logging
from enum import Enum
from typing import Dict, Set

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, AnyHttpUrl
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RecipeType(str, Enum):
    breakfast = "breakfast"
    snack = "snack"
    lunch = "lunch"
    dinner = "dinner"


class Recipe(BaseModel):
    name: str
    link: AnyHttpUrl
    recipe_types: Set[RecipeType]

    class Config:
        schema_extra = {
            "example": {
                "name": "Recipe",
                "link": "http://google.com",
                "recipe_types": {RecipeType.breakfast},
            }
        }


in_memory_db: Dict[int, Recipe] = dict()
id_counter: int = 0


@app.get("/recipes/")
def get_all_recipes():
    return in_memory_db


@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    if recipe_id not in in_memory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return in_memory_db[recipe_id]


@app.post("/recipes/")
def create_recipe(recipe: Recipe):
    global id_counter
    new_counter = id_counter = id_counter + 1
    in_memory_db[new_counter] = recipe
    logging.info(f"new counter: {new_counter} global counter: {id_counter}")
    return new_counter


@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    if recipe_id not in in_memory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    in_memory_db[recipe_id] = recipe
    return in_memory_db[recipe_id]


@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    if recipe_id not in in_memory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del in_memory_db[recipe_id]
