from app.crud.base import CRUDBase
from app.models.user_and_resource import User_And_Resource
from app.schemas.user_and_resource import UserAndResourceCreate, UserAndResourceUpdate


class CRUDUserAndResource(CRUDBase[User_And_Resource, UserAndResourceCreate, UserAndResourceUpdate]):
    ...


user_and_resource = CRUDUserAndResource(User_And_Resource)
