from importlib.resources import Resource
import uvicorn
from app.models.user import User
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends, Response
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from app.schemas.resource import ResourceCreate
from app.utils import fastapiTagsMetadata
from sqlalchemy.orm import Session
from typing import Optional, Any
from pathlib import Path
from app.schemas.resource import ResourceSearchResults, Resource, ResourceCreate
from app.schemas.user import User, UserCreate
import app.deps as deps
import app.crud as crud


srRouter = APIRouter(
    prefix="/shared-resources",
    tags=["shared-resources"],
    responses={404: {"description": "Not found"}},
)

mainApi = FastAPI(title="Shared Resource API", openapi_tags = fastapiTagsMetadata)



@mainApi.get("/resource/{resource_id}", status_code=200, response_model=Resource)
def fetch_resource(
    *,
    resource_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = crud.resource.get(db=db, id=resource_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Resource with ID {resource_id} not found"
        )

    return result

@mainApi.put("/resource/{resource_id}", status_code=200, response_model=str)
def delete_resource(
    *, resource_id: int, db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete a resource in the database.
    """
    result = crud.resource.get(db=db, id=resource_id)
    
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Resource with ID {resource_id} not found"
        )
    else:
        db.delete(result)
        db.commit()
        return f"Resource with ID {resource_id} has been deleted."


@mainApi.put("/user/{user_id}", status_code=200, response_model=str)
def delete_user(
    *, user_id: int, db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete a resource in the database.
    """
    result = crud.user.get(db=db, id=user_id)
    
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )
    else:
        db.delete(result)
        db.commit()
        return f"User with ID {user_id} has been deleted."


@mainApi.get("/user/{user_id}", status_code=200, response_model=User)
def fetch_user(
    *,
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single user by ID
    """
    result = crud.user.get(db=db, id=user_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    return result


@mainApi.post("/user/", status_code=201, response_model=User)
def create_user(
    *, db: Session = Depends(deps.get_db), user_in: UserCreate
) -> dict:
    """
    Create a new resource in the database.
    """
    user = crud.user.create(db=db, obj_in=user_in)

    return user

@mainApi.post("/resource/", status_code=201, response_model=Resource)
def create_resource(
    *, resource_in: ResourceCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new resource in the database.
    """
    resource = crud.resource.create(db=db, obj_in=resource_in)

    return resource




mainApi.include_router(srRouter)

if __name__ == "__main__":
    uvicorn.run(mainApi)
