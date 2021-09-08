import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_CONN_STRING = os.environ.get("MONGO_CONN_STRING")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONN_STRING)
database = client.stac
stac_collection = database.get_collection("stac_collection")
stac_item = database.get_collection("stac_item")

async def add_collection(new_collection: dict):
    collection = await stac_collection.insert_one(new_collection)

async def add_item(new_item: dict):
    item = await stac_collection.insert_one(new_item)

async def get_collections():
    collections = []
    async for collection in stac_collection.find():
        if "content" in collection:
            collections.append(collection["content"])
    return collections

async def get_one_collection(id: str):
    if (collection := await stac_collection.find_one({"_id": id})) is not None:
        return collection
    else:
        return {id: "Not found"}

async def get_item_collection(id: str):
    items = []
    async for item in stac_item.find({"_id": id}):
        if "content" in item:
            items.append(item["content"])
    return items