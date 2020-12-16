from fastapi import FastAPI

from src.routers import api

app = FastAPI()


app.include_router(api.api_router)
