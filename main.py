import uvicorn
from model import User
from fastapi import FastAPI, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from utils import fastapiTagsMetadata
from shared_resource_api import router as srRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, subqueryload
from model import base


mainApi = FastAPI(openapi_tags = fastapiTagsMetadata)
mainApi.include_router(srRouter)

db_string = "postgresql+psycopg2://ptjplqubrntdot:869c995e8c02bfda8f71d2c63eb361b105d7766a286ea9c27a871d3851b14c7a@ec2-52-209-185-5.eu-west-1.compute.amazonaws.com:5432/d1fsbmu87r2djb"
db = create_engine(db_string)
Session = sessionmaker(db)
base.metadata.create_all(db)

@mainApi.get("/hello-world")
def hello_world():
    return "Hello World! - First Commit ;)"


get_current_user = FirebaseCurrentUser(project_id = "sharet-a77e0")
'''An api to get current user data.
Args:
Valid ID Token
Returns:
A json response containing the user id of the current user
'''
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


if __name__ == "__main__":
    uvicorn.run(mainApi)
