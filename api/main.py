from fastapi import FastAPI
from dotenv import load_dotenv
import os
from .routers import stac_router
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
app = FastAPI()

app.include_router(stac_router.router)

# @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncIOMotorClient(os.getenv('DB_URL'))
#     app.mongodb = app.mongodb_client[os.getenv('DB_NAME')]

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()