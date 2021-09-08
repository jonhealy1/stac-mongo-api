import motor.motor_asyncio

MONGO_DETAILS = "mongodb://dev:stac@mongo:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.stac

stac_collection = database.get_collection("stac_collection")

async def add_collection(new_collection: dict):
    collection = await stac_collection.insert_one(new_collection)
    return collection

async def get_collections():
    collections = []
    async for collection in stac_collection.find():
        collections.append(collection)
    return collections