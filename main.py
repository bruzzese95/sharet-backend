from importlib.resources import Resource
import uvicorn
from app.models.user import User
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from app.schemas.resource import ResourceCreate
from app.utils import fastapiTagsMetadata
from sqlalchemy.orm import Session
from typing import Optional, Any
from pathlib import Path
from app.schemas.resource import ResourceSearchResults, Resource, ResourceCreate
import app.deps as deps
import app.crud as crud


srRouter = APIRouter(
    prefix="/shared-resources",
    tags=["shared-resources"],
    responses={404: {"description": "Not found"}},
)

mainApi = FastAPI(title="Shared Resource API", openapi_tags = fastapiTagsMetadata)


@mainApi.get("/hello-world")
def hello_world():
    return "Hello World! - First Commit ;)"


'''An api to get current user data.
Args:
Valid ID Token
Returns:
A json response containing the user id of the current user
'''
'''
get_current_user = FirebaseCurrentUser(project_id = "sharet-a77e0")
@mainApi.get("/user/")
def get_user(current_user: FirebaseClaims = Depends(get_current_user)):
    # ID token is valid and getting user info from ID token
    return {"id": current_user.user_id}


@mainApi.get("/user/{id}/")
def get_id(id: int):
    session = Session()
    user = session.query(User).filter(User.id == id).first()
    session.close()
    return user
'''

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


@mainApi.post("/resource/", status_code=201, response_model=Resource)
def create_resource(
    *, db: Session = Depends(deps.get_db), resource_in: ResourceCreate
) -> dict:
    """
    Create a new resource in the database.
    """
    resource = crud.resource.create(db=db, obj_in=resource_in)

    return resource



mainApi.include_router(srRouter)

if __name__ == "__main__":
    uvicorn.run(mainApi)
