import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://dev:stac@mongo:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.stac

stac_collection = database.get_collection("stac_collection")

async def add_collection(new_collection: dict):
    collection = await stac_collection.insert_one(new_collection)
    # return new_collection

async def get_collections():
    collections = []
    async for collection in stac_collection.find():
        collections.append(collection)
    return collections

async def get_collection(id: str):
    if (collection := await stac_collection.find_one({"_id": ObjectId(id)})) is not None:
        return collection
    else:
        return {id: "Not found"}