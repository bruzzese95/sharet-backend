from fastapi import FastAPI
import uvicorn


api = FastAPI()


@api.get("/hello-world")
def hello_world():
    return "Hello World! - First Commit ;)"


if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8080)
