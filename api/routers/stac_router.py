from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

router = APIRouter()

from api.db import (
    add_collection,
    add_item,
    get_collections,
    get_one_collection,
    get_item_collection
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
    collection = {"_id": content["id"], "content": content}
    collection = jsonable_encoder(collection)
    stac_collection = await add_collection(collection)

@router.post("/collections/{collection_id}")
async def post_item(content: dict):
    item = {"_id": content["id"], "content": content}
    item = jsonable_encoder(item)
    stac_item = await add_item(item)   

@router.get("/collections/{collection_id}")
async def get_collection(collection_id: str):
    collection_id = jsonable_encoder(collection_id)
    collection = await get_one_collection(collection_id)
    return collection

@router.get("/collections/{collection_id}/items")
async def get_items(collection_id: str):
    items = await get_item_collection(collection_id)
    if items:
        return items
    return {"error": "No items"}