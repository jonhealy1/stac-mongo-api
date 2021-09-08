from fastapi import FastAPI
import uvicorn
from .routers import stac_router
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

app.include_router(stac_router.router, tags=[])