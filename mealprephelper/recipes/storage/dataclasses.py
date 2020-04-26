from dataclasses import dataclass
from typing import List


@dataclass
class StorageRecipeType:
    recipe_type_id: int
    name: str
    color: str


@dataclass
class StorageIngredient:
    ingredient_id: int
    name: str


@dataclass
class StorageRecipeIngredient(StorageIngredient):
    amount: str
    unit: str


@dataclass
class StorageRecipe:
    recipe_id: int
    name: str
    link: str
    recipe_types: List[StorageRecipeType]
    ingredients: List[StorageRecipeIngredient]
