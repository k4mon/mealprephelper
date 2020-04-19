from fastapi import HTTPException
from sqlalchemy.orm import Session

from mealprephelper.recipes import models, schemas


def get_recipes(db: Session):
    return db.query(models.Recipe).all()


def get_recipe(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Item not found")
    return recipe


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    recipe_types = (
        db.query(models.RecipeType)
        .filter(models.RecipeType.name.in_(recipe.dict().pop("recipe_types", None)))
        .all()
    )
    db_recipe = models.Recipe(
        name=recipe.name, link=recipe.link, recipe_types=recipe_types
    )
    db.add(db_recipe)
    db.commit()
    return db_recipe


def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeCreate):
    db_recipe = get_recipe(db, recipe_id)
    for k, v in recipe.dict().items():
        if k == "recipe_types":
            v = (
                db.query(models.RecipeType)
                .filter(
                    models.RecipeType.name.in_(recipe.dict().pop("recipe_types", None))
                )
                .all()
            )
        setattr(db_recipe, k, v)
    db.commit()
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    db.delete(get_recipe(db, recipe_id))
    db.commit()
