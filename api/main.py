from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root_catalog():
    return {"root_catalog": "Hello World"}

@app.get("/collections")
async def get_all_collections():
    return {"all_collections": "All Collections"}

@app.get("/collections/{collection_id}")
async def get_collection(collection_id):
    return {"collection_id": collection_id}