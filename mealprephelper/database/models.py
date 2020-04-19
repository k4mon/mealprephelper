from mealprephelper.database.database import Base
from mealprephelper.recipes import models as recipes_models
from mealprephelper.users import models as user_models

# import all models for alembic
base = Base
recipes_models = recipes_models
user_models = user_models
