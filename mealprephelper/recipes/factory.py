from mealprephelper.recipes.service.interface import AbstractRecipeService
from mealprephelper.recipes.service.service import RecipeService
from mealprephelper.recipes.storage.storage import InMemoryRecipeStorage

storage = InMemoryRecipeStorage()


def create_recipe_service() -> AbstractRecipeService:
    return RecipeService(storage=storage)
