# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.resource import Resource  # noqa
from app.models.reservation import Reservation  # noqa
from app.models.user_and_resource import User_And_Resource  # noqa