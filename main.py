from fastapi import FastAPI
import uvicorn
from utils import fastapiTagsMetadata
from shared_resource_api import router as srRouter


mainApi = FastAPI(openapi_tags = fastapiTagsMetadata)
mainApi.include_router(srRouter)


@mainApi.get("/hello-world")
def hello_world():
    return "Hello World! - First Commit ;)"


if __name__ == "__main__":
    uvicorn.run(mainApi)
