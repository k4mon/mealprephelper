from typing import List

from mealprephelper.recipes.service.interface import AbstractRecipeService
from mealprephelper.recipes.schema import Ingredient, RecipeCreate, Recipe
from mealprephelper.recipes.storage.interface import AbstractRecipeStorage


class RecipeService(AbstractRecipeService):
    def __init__(self, storage: AbstractRecipeStorage):
        self.storage = storage

    def get_recipes(self) -> List[Recipe]:
        return self.storage.get_all_recipes()

    def get_recipe(self, recipe_id: int) -> Recipe:
        return self.storage.get_recipe_by_id(recipe_id)

    def create_recipe(self, recipe: RecipeCreate) -> Recipe:
        if self.storage.recipe_exists(recipe.name):
            raise Exception("Recipe with this name already exists")
        return self.storage.create_recipe(recipe)

    def update_recipe(self, recipe_id: int, recipe: RecipeCreate) -> Recipe:
        return self.storage.update_recipe(recipe_id, recipe)

    def delete_recipe(self, recipe_id: int) -> None:
        self.storage.delete_recipe(recipe_id)

    def get_ingredients(self) -> List[Ingredient]:
        return self.storage.get_all_ingredients()

    def delete_ingredient(self, ingredient_id: int) -> None:
        self.storage.delete_ingredient(ingredient_id)
