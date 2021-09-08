from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root_catalog():
    return {"root_catalog": "Hello World"}

@router.get("/collections")
async def get_all_collections():
    return {"all_collections": "All Collections"}

@router.get("/collections/{collection_id}")
async def get_collection(collection_id):
    return {"collection_id": collection_id}