from typing import List
from pydantic import BaseModel

class SharedResource(BaseModel):
    id: int = 123
    name: str = "Automobile"

class SharedResourceList(BaseModel):
    sharedResourceDtoList: List[SharedResource]