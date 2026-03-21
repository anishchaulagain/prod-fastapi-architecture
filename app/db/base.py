# This file's only job: import all models so Alembic can see them.
# If a model isn't imported here, Alembic won't generate a migration for it.
from app.db.base_class import Base       # noqa
from app.models.user import User         # noqa