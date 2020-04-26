from typing import List

from mealprephelper.recipes.schema import (
    Ingredient,
    Recipe,
    RecipeCreate,
    RecipeType,
    RecipeIngredient,
)
from mealprephelper.recipes.storage.in_memory.dataclasses import (
    StorageRecipeType,
    StorageRecipeIngredient,
    StorageRecipe,
    StorageIngredient,
)
from mealprephelper.recipes.storage.interface import AbstractRecipeStorage


class InMemoryRecipeStorage(AbstractRecipeStorage):
    RECIPES = []
    RECIPE_ID = 0
    INGREDIENTS = []
    INGREDIENT_ID = 0
    RECIPE_TYPES = [
        StorageRecipeType(recipe_type_id=0, name="breakfast", color="#008000"),
        StorageRecipeType(recipe_type_id=1, name="lunch", color="#000080"),
        StorageRecipeType(recipe_type_id=2, name="snack", color="#880000"),
        StorageRecipeType(recipe_type_id=3, name="dinner", color="#800080"),
    ]

    def _get_next_recipe_id(self):
        user_id = self.RECIPE_ID
        self.RECIPE_ID = self.RECIPE_ID + 1
        return user_id

    def _get_next_ingredient_id(self):
        user_id = self.INGREDIENT_ID
        self.INGREDIENT_ID = self.INGREDIENT_ID + 1
        return user_id

    @staticmethod
    def _map_recipe_types_from_dataclass(
        stored_recipe_types: List[StorageRecipeType],
    ) -> List[RecipeType]:
        return [
            RecipeType(
                id=stored_recipe_type.recipe_type_id,
                name=stored_recipe_type.name,
                color=stored_recipe_type.color,
            )
            for stored_recipe_type in stored_recipe_types
        ]

    @staticmethod
    def _map_ingredients_from_dataclass(
        stored_recipe_ingredients: List[StorageRecipeIngredient],
    ) -> List[RecipeIngredient]:
        return [
            RecipeIngredient(
                name=stored_recipe_ingredient.name,
                amount=stored_recipe_ingredient.amount,
                unit=stored_recipe_ingredient.unit,
            )
            for stored_recipe_ingredient in stored_recipe_ingredients
        ]

    def _map_recipe_types_to_dataclass(self, recipe_types: List[str]) -> List[StorageRecipeType]:
        return [
            storage_recipe_type
            for storage_recipe_type in self.RECIPE_TYPES
            if storage_recipe_type.name in recipe_types
        ]

    def _add_ingredients(
        self, ingredients: List[RecipeIngredient]
    ) -> List[StorageRecipeIngredient]:
        stored_recipe_ingredients = []
        for ingredient in ingredients:
            try:
                stored_ingredient = next(
                    stored_ingredient
                    for stored_ingredient in self.INGREDIENTS
                    if stored_ingredient.name == ingredient.name
                )
            except Exception:
                stored_ingredient = StorageIngredient(
                    ingredient_id=self._get_next_ingredient_id(), name=ingredient.name
                )
                self.INGREDIENTS.append(stored_ingredient)
            stored_recipe_ingredients.append(
                StorageRecipeIngredient(
                    ingredient_id=stored_ingredient.ingredient_id,
                    name=stored_ingredient.name,
                    amount=ingredient.amount,
                    unit=ingredient.unit,
                )
            )
        return stored_recipe_ingredients

    def get_all_recipes(self) -> List[Recipe]:
        return [
            Recipe(
                id=recipe.recipe_id,
                name=recipe.name,
                link=recipe.link,
                recipe_types=self._map_recipe_types_from_dataclass(recipe.recipe_types),
                ingredients=self._map_ingredients_from_dataclass(recipe.ingredients),
            )
            for recipe in self.RECIPES
        ]

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        stored_recipe = next(
            stored_recipe for stored_recipe in self.RECIPES if stored_recipe.recipe_id == recipe_id
        )
        return Recipe(
            id=stored_recipe.recipe_id,
            name=stored_recipe.name,
            link=stored_recipe.link,
            recipe_types=self._map_recipe_types_from_dataclass(stored_recipe.recipe_types),
            ingredients=self._map_ingredients_from_dataclass(stored_recipe.ingredients),
        )

    def recipe_exists(self, recipe_name: str) -> bool:
        return any([recipe for recipe in self.RECIPES if recipe.name == recipe_name])

    def create_recipe(self, recipe: RecipeCreate) -> Recipe:
        stored_recipe = StorageRecipe(
            recipe_id=self._get_next_recipe_id(),
            name=recipe.name,
            link=recipe.link,
            recipe_types=self._map_recipe_types_to_dataclass(recipe.recipe_types),
            ingredients=self._add_ingredients(recipe.ingredients),
        )
        self.RECIPES.append(stored_recipe)
        return Recipe(
            id=stored_recipe.recipe_id,
            name=stored_recipe.name,
            link=stored_recipe.link,
            recipe_types=self._map_recipe_types_from_dataclass(stored_recipe.recipe_types),
            ingredients=self._map_ingredients_from_dataclass(stored_recipe.ingredients),
        )

    def update_recipe(self, recipe_id: int, recipe: RecipeCreate) -> Recipe:
        self.delete_recipe(recipe_id)
        stored_recipe = StorageRecipe(
            recipe_id=recipe_id,
            name=recipe.name,
            link=recipe.link,
            recipe_types=self._map_recipe_types_to_dataclass(recipe.recipe_types),
            ingredients=self._add_ingredients(recipe.ingredients),
        )
        self.RECIPES.append(stored_recipe)
        return Recipe(
            id=stored_recipe.recipe_id,
            name=stored_recipe.name,
            link=stored_recipe.link,
            recipe_types=self._map_recipe_types_from_dataclass(stored_recipe.recipe_types),
            ingredients=self._map_ingredients_from_dataclass(stored_recipe.ingredients),
        )

    def delete_recipe(self, recipe_id: int) -> None:
        for recipe in self.RECIPES:
            if recipe.recipe_id == recipe_id:
                self.RECIPES.remove(recipe)
                return None

    def get_all_ingredients(self) -> List[Ingredient]:
        return [
            Ingredient(id=storage_ingredient.ingredient_id, name=storage_ingredient.name)
            for storage_ingredient in self.INGREDIENTS
        ]

    def delete_ingredient(self, ingredient_id: int) -> None:
        for ingredient in self.INGREDIENTS:
            if ingredient.ingredient_id == ingredient_id:
                self.INGREDIENTS.remove(ingredient)
                return None

    def get_recipe_types_names(self) -> List[str]:
        return [recipe_type.name for recipe_type in self.RECIPE_TYPES]
