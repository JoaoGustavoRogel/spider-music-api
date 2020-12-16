import os
import shutil

from fastapi import APIRouter, HTTPException
from datetime import datetime

from src.models.SpotifyCrawler import ConcreteFactorySpotifyChartsCrawler



router = APIRouter()

@router.get("/chart")
def get_data_chart(start_date: str, end_date: str):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        print(start_date, end_date)

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
