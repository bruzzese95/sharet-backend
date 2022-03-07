from pydantic import BaseModel

class SharedResource(BaseModel):
    id: int = 123
    name: str = "Automobile"