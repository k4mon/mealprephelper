from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from mealprephelper.config import origins
from mealprephelper.database.database import engine, SessionLocal
from mealprephelper.recipes import models, schemas, service

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recipes/", response_model=List[schemas.Recipe])
def get_recipes(db: Session = Depends(get_db)):
    return service.get_recipes(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return service.get_recipe(db, recipe_id)


@app.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    return service.create_recipe(db, recipe)


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(
    recipe_id: int, recipe: schemas.Recipe, db: Session = Depends(get_db)
):
    return service.update_recipe(db, recipe_id, recipe)


@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return service.delete_recipe(db, recipe_id)
