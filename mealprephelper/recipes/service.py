from fastapi import HTTPException
from sqlalchemy.orm import Session

from mealprephelper.recipes import models, schemas


def get_recipes(db: Session):
    recipes = []
    db_recipes = db.query(models.Recipe).all()
    for db_recipe in db_recipes:
        ingredients = []
        for ingredient in db_recipe.ingredients:
            ingredients.append(
                schemas.RecipeIngredient(name=ingredient.ingredient.name, amount=ingredient.amount)
            )
        recipes.append(
            schemas.Recipe(
                id=db_recipe.id,
                name=db_recipe.name,
                link=db_recipe.link,
                recipe_types=db_recipe.recipe_types,
                ingredients=ingredients,
            )
        )
    return recipes


def get_recipe(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Item not found")
    return recipe


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    recipe_types = _prepare_recipe_types(db, recipe.dict().pop("recipe_types", None))
    recipe_ingredients = _prepare_recipe_ingredients(db, recipe.dict().pop("ingredients", []))
    db_recipe = models.Recipe(
        name=recipe.name,
        link=recipe.link,
        recipe_types=recipe_types,
        ingredients=recipe_ingredients,
    )
    db.add(db_recipe)
    db.commit()
    return db_recipe


def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeCreate):
    db_recipe = get_recipe(db, recipe_id)
    for k, v in recipe.dict().items():
        if k == "recipe_types":
            v = _prepare_recipe_types(db, recipe.dict().pop("recipe_types", None))
        elif k == "ingredients":
            v = _prepare_recipe_ingredients(db, recipe.dict().pop("ingredients", []))
        setattr(db_recipe, k, v)
    db.commit()
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    db.delete(get_recipe(db, recipe_id))
    db.commit()


def get_ingredients(db: Session):
    return db.query(models.Ingredient).all()


def get_ingredient(db: Session, recipe_id: int):
    ingredient = db.query(models.Ingredient).filter(models.Ingredient.id == recipe_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Item not found")
    return ingredient


def create_ingredient(db: Session, ingredient: schemas.IngredientBase):
    db_ingredient = models.Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    return db_ingredient


def delete_ingredient(db: Session, ingredient_id: int):
    db.delete(get_ingredient(db, ingredient_id))
    db.commit()


def _prepare_recipe_types(db, recipe_type_ids):
    return db.query(models.RecipeType).filter(models.RecipeType.name.in_(recipe_type_ids)).all()


def _prepare_recipe_ingredients(db, ingredients):
    db_recipe_ingredients = []
    for ingredient in ingredients:
        db_ingredient = (
            db.query(models.Ingredient)
            .filter(models.Ingredient.name == ingredient["name"])
            .first()
        )
        db_recipe_ingredients.append(
            models.RecipeIngredients(ingredient=db_ingredient, amount=ingredient["amount"],)
        )
    return db_recipe_ingredients
