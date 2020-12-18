from fastapi import APIRouter

from src.routers.endpoints import test
from src.routers.endpoints import spotify_chart, spotify_api

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(spotify_chart.router, prefix="/spotify/chart")
api_router.include_router(spotify_api.router, prefix="/spotify/api")

