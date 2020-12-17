from fastapi import APIRouter

from src.routers.endpoints import test
from src.routers.endpoints import spotify_chart

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(spotify_chart.router, prefix="/spotify")

