# Import all the models, so that Base has them before being
# imported by Alembic
from sharetbackend.app.db.base_class import Base  # noqa
from sharetbackend.app.models.user import User  # noqa
from sharetbackend.app.models.resource import Resource  # noqa
