from fastapi import APIRouter

router = APIRouter()

from api.db import (
    get_collections
)

@router.get("/")
async def root_catalog():
    return {"root_catalog": "Hello World"}

@router.get("/collections")
async def get_all_collections():
    collections = await get_collections()
    if collections:
        return collections
    return {"error": "No collections"}

@router.get("/collections/{collection_id}")
async def get_collection(collection_id):
    return {"collection_id": collection_id}