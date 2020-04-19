from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from mealprephelper.database.database import Base

recipe_recipe_types_association_table = Table(
    "recipe_recipe_types_association_table",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id")),
    Column("recipe_type_id", Integer, ForeignKey("recipe_types.id")),
)


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    link = Column(String)

    recipe_types = relationship(
        "RecipeType",
        secondary=recipe_recipe_types_association_table,
        back_populates="recipes",
    )


class RecipeType(Base):
    __tablename__ = "recipe_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    recipes = relationship(
        "Recipe",
        secondary=recipe_recipe_types_association_table,
        back_populates="recipe_types",
    )
