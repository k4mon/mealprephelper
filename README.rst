To generate migrations:
 - start containers with ``docker-compose up --build``
 - get into the mealprephelper container
 - change directory to /app/alembic
 - execute ``alembic revision --autogenerate -m "<MIGRATION_MESSAGE>"``

To execute migrations:
 - start containers with ``docker-compose up --build``
 - get into the mealprephelper container
 - change directory to /app/alembic
 - execute ``alembic upgrade head`