from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/collections/{collection_id}")
async def get_collection(collection_id):
    return {"collection_id": collection_id}