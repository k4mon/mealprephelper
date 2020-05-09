from typing import List

from mealprephelper.recipes.service.interface import AbstractRecipeService
from mealprephelper.recipes.schema import Ingredient, RecipeCreate, Recipe, RecipeType
from mealprephelper.recipes.storage.interface import AbstractRecipeStorage


class RecipeService(AbstractRecipeService):
    def __init__(self, storage: AbstractRecipeStorage):
        self.storage = storage

    def get_recipes(self, username: str) -> List[Recipe]:
        return self.storage.get_all_recipes(username)

    def get_recipe(self, username: str, recipe_id: int) -> Recipe:
        return self.storage.get_recipe_by_id(username, recipe_id)

    def create_recipe(self, username: str, recipe: RecipeCreate) -> Recipe:
        if self.storage.recipe_exists(username, recipe.name):
            raise Exception("Recipe with this name already exists")
        return self.storage.create_recipe(username, recipe)

    def update_recipe(self, username: str, recipe_id: int, recipe: RecipeCreate) -> Recipe:
        return self.storage.update_recipe(username, recipe_id, recipe)

    def delete_recipe(self, username: str, recipe_id: int) -> None:
        self.storage.delete_recipe(username, recipe_id)

    def get_recipe_types(self, username: str) -> List[RecipeType]:
        return self.storage.get_recipe_types(username)

    def get_ingredients(self) -> List[Ingredient]:
        return self.storage.get_all_ingredients()

    def delete_ingredient(self, ingredient_id: int) -> None:
        self.storage.delete_ingredient(ingredient_id)
