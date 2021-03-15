from fastapi import FastAPI
from server.routes.light_route import router as LightRouter


app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to my API!"}

app.include_router(LightRouter, tags=["Light"], prefix="/light")