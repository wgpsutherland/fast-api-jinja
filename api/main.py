from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import explore

app = FastAPI()

app.mount("/static", StaticFiles(directory="api/static"), name="static")

app.include_router(explore.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
