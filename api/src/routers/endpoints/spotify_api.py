import os
import shutil

from fastapi import APIRouter, HTTPException
from datetime import datetime

from src.models.SpotifyAPICrawler import ConcreteFactorySpotifyAPICrawler
from src.models.MySql import MySql


router = APIRouter()
mysql_db = MySql.instance()
factory = ConcreteFactorySpotifyAPICrawler()


def __query_data_crawler(query_type, query_id):
    crwl = factory.create_crawler()
    query_data = {
        "query_type": query_type,
        "query": query_id,
        "path": "outputs"
    }
    data = crwl.get_data(query_data)
    return data

@router.get("/crawler_track")
def query_crawler_track_by_id(id: str):
    crawler_data = __query_data_crawler("track_by_id", id)

    return {"data": crawler_data}

@router.get("/crawler_artist")
def query_crawler_artist_by_id(id: str):
    crawler_data = __query_data_crawler("artist_by_id", id)

    return {"data": crawler_data}

@router.get("/crawler_album")
def query_crawler_album_by_id(id: str):
    crawler_data = __query_data_crawler("album_by_id", id)

    return {"data": crawler_data}

@router.get("/insert_album")
def insert_album_db(id: str):
    collected_data = __query_data_crawler("album_by_id", id)

    fields = ["album_id", "album_name", "album_url", "total_tracks", "release_date", "artist_id", "popularity", "label"]    

    for item in collected_data:
        for key in fields:
            if key not in item:
                item[key] = "None"

    mysql_db.insert_data_list("src/sql/insert_album_api.sql", collected_data)

    return {"message": "Sucess, welcome data!"}

@router.get("/insert_track")
def insert_track_db(id: str):
    collected_data = __query_data_crawler("track_by_id", id)

    fields = ["track_id", "track_name", "track_url", "disc_number", "duration_ms", "artist_id", "track_number", "popularity", "album_id"]

    for item in collected_data:
        for key in fields:
            if key not in item:
                item[key] = "None"

    mysql_db.insert_data_list("src/sql/insert_track_api.sql", collected_data)

    return {"message": "Sucess, welcome data!"}

@router.get("/insert_artist")
def insert_artist_db(id: str):
    collected_data = __query_data_crawler("artist_by_id", id)

    fields = ["artist_id", "artist_name", "artist_url", "track_number", "disc_number", "popularity", "followers"]

    for item in collected_data:
        for key in fields:
            if key not in item:
                item[key] = "None"

    mysql_db.insert_data_list("src/sql/insert_artist_api.sql", collected_data)

    return {"message": "Sucess, welcome data!"}

def __delete_data_from_db(sql_file, id):
    params = [id]
    mysql_db.delete_data(sql_file, params)

    return {"message": "Sucess, good bye data!"}

@router.get("/delete_artist")
def delete_artist_db(id: str):
    return __delete_data_from_db("src/sql/delete_artist_api.sql", id)

@router.get("/delete_album")
def delete_album_db(id: str):
    return __delete_data_from_db("src/sql/delete_album_api.sql", id)

@router.get("/delete_track")
def delete_track_db(id: str):
    return __delete_data_from_db("src/sql/delete_track_api.sql", id)

# def __update_data_from_db(query_type)

