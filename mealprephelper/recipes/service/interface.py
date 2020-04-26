import abc
from typing import List

from mealprephelper.recipes.service.schema import Recipe, Ingredient, RecipeCreate


class AbstractRecipeService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_recipes(self) -> List[Recipe]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_recipe(self, recipe_id: int) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def create_recipe(self, recipe: RecipeCreate) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def update_recipe(self, recipe_id: int, recipe: RecipeCreate) -> Recipe:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_recipe(self, recipe_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ingredients(self) -> List[Ingredient]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_ingredient(self, ingredient_id: int) -> None:
        raise NotImplementedError
