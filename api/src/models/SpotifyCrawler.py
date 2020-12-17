from __future__ import annotations

import concurrent.futures
import json
from datetime import datetime, timedelta
from operator import itemgetter

import pandas as pd
import requests
from src.constants import FILTERS, NA
from src.schemas.Crawler import AbstractCrawler, AbstractFactory


class ConcreteFactorySpotifyChartsCrawler(AbstractFactory):
    def create_crawler(self) -> AbstractCrawler:
        return ConcreteSpotifyChartsCrawler()


class ConcreteSpotifyChartsCrawler(AbstractCrawler):
    def request_data(self, params):

        date = params["date"]
        path = params["path"]
        period = params["period"]
        region = params["region"]
        chart_type = params["chart_type"]
        filename = f"{path}/spotify_charts_{region}_{date}.csv"

        url = (
            f"https://spotifycharts.com/{chart_type}/{region}/{period}/{date}/download"
        )

        print(f"Baixando o arquivo na url: {url}")

        try:
            r = requests.get(url, stream=True)
            with open(filename, "wb") as fd:
                for chunk in r.iter_content(2000):
                    fd.write(chunk)

            print(f"Arquivo baixado com sucesso em {filename}")

            if chart_type == "viral":
                df = pd.read_csv(filename)
            elif chart_type == "regional":
                df = pd.read_csv(filename, skiprows=1)

            return df
        except Exception as e:
            raise Exception(
                f"Não foi possível baixar o arquivo {filename} na url {url}: {e}"
            )

    def process_data(self, data, params):

        print(f"Exibindo dataframe coletado:\n{data}")

        date = params["date"].split("--")[0]
        period = params["period"]
        region = params["region"].replace("regional/", "")
        chart_type = params["chart_type"].replace("/", "")

        if chart_type == "viral":
            data.columns = ["position", "track_name", "artist_name", "url"]
            data["streams"] = data.apply(lambda row: NA, axis=1)

        elif chart_type == "regional":
            data.columns = ["position", "track_name", "artist_name", "streams", "url"]

        data["track_id"] = data.apply(
            lambda row: row["url"].split("track/")[-1], axis=1
        )
        data["chart_type"] = data.apply(lambda row: chart_type, axis=1)
        data["date"] = data.apply(lambda row: date, axis=1)
        data["period"] = data.apply(lambda row: period, axis=1)
        data["region"] = data.apply(lambda row: region, axis=1)

        print(f"Exibindo dataframe processado:\n{data}")

        tidy_data = data.to_dict("records")
        return tidy_data

    def get_data(self, params):

        tidy = []
        dates_to_collect = []
        date = params["start_date"]
        stop = params["end_date"]
        path = params["path"]

        while date != stop:
            dates_to_collect.append(date.strftime("%Y-%m-%d"))
            date = date + timedelta(days=1)

        if "2017-02-23" in dates_to_collect:
            dates_to_collect.remove("2017-02-23")
        if "2017-05-30" in dates_to_collect:
            dates_to_collect.remove("2017-05-30")
        if "2017-05-31" in dates_to_collect:
            dates_to_collect.remove("2017-05-31")
        if "2017-06-02" in dates_to_collect:
            dates_to_collect.remove("2017-06-02")

        collect_info = []
        self.clear_folder(path)

        for region in FILTERS["region"]:
            for date in dates_to_collect:
                collect_info.append({"date": date, "region": region, "path": path})

        with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
            future_to_info = {
                executor.submit(self.processing_helper, info): info
                for info in collect_info
            }
            for future in concurrent.futures.as_completed(future_to_info):
                info = future_to_info[future]
                try:
                    tidy += future.result()
                except Exception as e:
                    raise Exception(
                        f"Não foi possível processar os dados para os seguintes parâmetros: {info}\n{e}"
                    )

        self.clear_folder(path)
        tidy = sorted(tidy, key=itemgetter("region", "date", "position"))
        print(f"Exibindo dados coletados:\n{tidy}")

        return tidy

    def processing_helper(self, info):
        params = {
            "date": info["date"],
            "period": "daily",
            "region": info["region"],
            "chart_type": "regional",
            "path": info["path"],
        }
        try:
            df = self.request_data(params)
            tidy = self.process_data(df, params)
            return tidy
        except Exception as e:
            raise Exception(
                f"Não foi possível processar os dados para os seguintes parâmetros: {params}\n{e}"
            )


"""
# Exemplo do funcionamento
def client_code(factory: AbstractFactory) -> None:
    crwl = factory.create_crawler()
    data = crwl.get_data({
        "start_date": datetime(2020, 12, 10),
        "end_date": datetime(2020, 12, 13),
        "path": "outputs"
    })


if __name__ == "__main__":
    print("Testando o crawler Spotify Charts")
    client_code(ConcreteFactorySpotifyChartsCrawler())
"""
