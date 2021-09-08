from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()

from api.db import (
    get_collections,
    add_collection
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
async def post_collection(id):
    collection = {"_id": id, "hello":"world"}
    collection = jsonable_encoder(collection)
    stac_collection = await add_collection(collection)
    created_student = await get_collections()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)

@router.get("/collections/{collection_id}")
async def get_collection(collection_id):
    return {"collection_id": collection_id}