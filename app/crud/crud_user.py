from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[User]:
        return db.query(User).filter(User.name == name).first()

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


    def update_user(self, *, db: Session, user: User):

        # get the existing data
        db_user = db.query(User).filter(User.idToken == user.idToken).one_or_none()
        if db_user is None:
            return None

        # Update model class variable from requested fields 
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user = CRUDUser(User)
