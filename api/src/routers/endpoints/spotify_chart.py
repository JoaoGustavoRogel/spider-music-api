import os
import shutil

from fastapi import APIRouter, HTTPException
from datetime import datetime

from src.models.SpotifyCrawler import ConcreteFactorySpotifyChartsCrawler
from src.models.MySql import MySql


router = APIRouter()


@router.get("/crawler_query")
def get_data_chart(start_date: str, end_date: str):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except Exception:
        raise HTTPException(status_code=201, detail="Invalid date format. Must be: YYYY-MM-DD")

    factory = ConcreteFactorySpotifyChartsCrawler()
    crawler = factory.create_crawler()
    path = "outputs/"

    data_to_extract = {
        "start_date": start_date,
        "end_date": end_date,
        "path": path,
    }

    try:
        shutil.rmtree(path)
    except Exception:
        pass
        
    os.mkdir(path)
    collected_data = crawler.get_data(data_to_extract)
    shutil.rmtree(path)

    return {"data": collected_data}

@router.get("/insert_db")
def insert_data_db(start_date: str, end_date: str):
    mysql_db = MySql.instance()
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except Exception:
        raise HTTPException(status_code=201, detail="Invalid date format. Must be: YYYY-MM-DD")

    factory = ConcreteFactorySpotifyChartsCrawler()
    crawler = factory.create_crawler()
    path = "outputs/"

    data_to_extract = {
        "start_date": start_date,
        "end_date": end_date,
        "path": path,
    }

    try:
        shutil.rmtree(path)
    except Exception:
        pass
        
    os.mkdir(path)
    collected_data = crawler.get_data(data_to_extract)
    shutil.rmtree(path)

    try:
        mysql_db.insert_data_list("src/sql/insert_spotify_chart.sql", collected_data)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intern error!")

    return {"message": "Sucess in insert, welcome data!"}

@router.get("/query_db")
def query_data_db(start_date: str, end_date: str):
    mysql_db = MySql.instance()
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except Exception:
        raise HTTPException(status_code=201, detail="Invalid date format. Must be: YYYY-MM-DD")

    parameters = [start_date, end_date]
    res_query = mysql_db.query_data("src/sql/query_spotify_chart.sql", parameters)
    fields = ["position","track_name","artist_name","streams","url","track_id","chart_type","date","period","region"]


    return {"fields": fields, "count_data": len(res_query), "data": res_query}

@router.get("/delete_db")
def delete_data_db(start_date: str, end_date: str):
    mysql_db = MySql.instance()
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except Exception:
        raise HTTPException(status_code=201, detail="Invalid date format. Must be: YYYY-MM-DD")

    parameters = [start_date, end_date]
    mysql_db.delete_data("src/sql/delete_spotify_chart.sql", parameters)

    return {"message": "Sucess, good bye data!"}

@router.get("/update_db")
def update_data_db(start_date: str, end_date: str):
    mysql_db = MySql.instance()
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except Exception:
        raise HTTPException(status_code=201, detail="Invalid date format. Must be: YYYY-MM-DD")

    parameters = [start_date, end_date]
    mysql_db.delete_data("src/sql/delete_spotify_chart.sql", parameters)
    
    factory = ConcreteFactorySpotifyChartsCrawler()
    crawler = factory.create_crawler()
    path = "outputs/"

    data_to_extract = {
        "start_date": datetime.strptime(start_date, "%Y-%m-%d"),
        "end_date": datetime.strptime(end_date, "%Y-%m-%d"),
        "path": path,
    }

    try:
        shutil.rmtree(path)
    except Exception:
        pass
        
    os.mkdir(path)
    collected_data = crawler.get_data(data_to_extract)
    shutil.rmtree(path)

    mysql_db.insert_data_list("src/sql/insert_spotify_chart.sql", collected_data)

    return {"message": "Sucess, welcome new data!"}
