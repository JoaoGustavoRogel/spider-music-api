import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from src.models.MySql import MySql
from src.routers import api

app = FastAPI()
mysql_db = MySql.instance()

app.include_router(api.api_router)
