"""added ingredients

Revision ID: b6db6de24895
Revises: 1b61dc8f4ffe
Create Date: 2020-04-19 18:15:04.875199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b6db6de24895"
down_revision = "1b61dc8f4ffe"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ingredients",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ingredients_id"), "ingredients", ["id"], unique=False)
    op.create_table(
        "recipe_ingredients",
        sa.Column("recipe_id", sa.Integer(), nullable=False),
        sa.Column("ingredient_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["ingredient_id"], ["ingredients.id"],),
        sa.ForeignKeyConstraint(["recipe_id"], ["recipes.id"],),
        sa.PrimaryKeyConstraint("recipe_id", "ingredient_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("recipe_ingredients")
    op.drop_index(op.f("ix_ingredients_id"), table_name="ingredients")
    op.drop_table("ingredients")
    # ### end Alembic commands ###
