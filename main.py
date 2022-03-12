import uvicorn
from fastapi import FastAPI, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from utils import fastapiTagsMetadata
from shared_resource_api import router as srRouter


mainApi = FastAPI(openapi_tags = fastapiTagsMetadata)
mainApi.include_router(srRouter)


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


if __name__ == "__main__":
    uvicorn.run(mainApi)
