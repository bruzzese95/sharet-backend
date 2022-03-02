from fastapi import APIRouter


router = APIRouter(
    prefix="/shared-resources",
    tags=["shared-resources"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{res_id}", summary="Retrive the whole data of a specific shared resource")
def get_shared_resources_res_id(id: int):
    return f"Implement the CRUD for resource with id: {id}"