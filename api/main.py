from fastapi import FastAPI
from dotenv import load_dotenv
from .routers import stac_router
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.include_router(stac_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],      
)