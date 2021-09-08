from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

router = APIRouter()

from api.db import (
    get_collections,
    add_collection,
    get_one_collection
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

@router.post("/collections/")
async def post_collection(content: dict):
    collection = {"_id": content["id"], "collection": content}
    collection = jsonable_encoder(collection)
    stac_collection = await add_collection(collection)
    created_student = await get_collections()
    return created_student

@router.get("/collections/{collection_id}")
async def get_collection(collection_id: str):
    collection_id = jsonable_encoder(collection_id)
    collection = await get_one_collection(collection_id)
    return collection