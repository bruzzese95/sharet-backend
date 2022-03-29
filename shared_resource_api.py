from typing import List
from fastapi import APIRouter

from model import SharedResource, SharedResourceList

fake_db = [
    SharedResource(id=1, name="Grande Punto di Antonio"),
    SharedResource(id=2, name="Moto di Sara"),
    SharedResource(id=3, name="Bicicletta di Andrea")
]


router = APIRouter(
    prefix="/shared-resources",
    tags=["shared-resources"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{res_id}", summary="Retrive the whole data of a specific shared resource identified by its id")
def get_shared_resources_res_id(id: int) -> SharedResource:
    for r in fake_db:
        if(r.id == id):
            return r

    return SharedResource()

@router.get("/", summary="Retrive all the shared resources")
def get_shared_resources() -> SharedResourceList:
    list = SharedResourceList(sharedResourceDtoList = fake_db)
    return list