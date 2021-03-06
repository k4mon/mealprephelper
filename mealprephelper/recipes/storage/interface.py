import abc
from typing import List

from mealprephelper.recipes.schema import Recipe, Ingredient, RecipeCreate, RecipeType


class AbstractRecipeStorage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_all_recipes(self, username: str) -> List[Recipe]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_recipe_by_id(self, username: str, recipe_id: int) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def recipe_exists(self, username: str, recipe_name: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def create_recipe(self, username: str, recipe: RecipeCreate) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def update_recipe(self, username: str, recipe_id: int, recipe: RecipeCreate) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_recipe(self, username: str, recipe_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_recipe_types(self, username: str) -> List[RecipeType]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_ingredients(self) -> List[Ingredient]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ingredient(self, ingredient_id: int) -> None:
        raise NotImplementedError
