import os

import mysql.connector
# Debug
from dotenv import load_dotenv

load_dotenv()
# End Debug


class MySql:
    _instance = None

    def __init__(self):
        self.__credentials = self.__get_credentials()
        user = self.__credentials["user"]
        password = self.__credentials["password"]
        host = self.__credentials["host"]
        database = self.__credentials["database"]

        self.__cnx = mysql.connector.connect(
            user=user, password=password, host=host, database=database
        )
        self.__cursor = self.__cnx.cursor()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def __get_credentials(self):
        credentials = {
            "user": os.getenv("USER_MYSQL"),
            "password": os.getenv("PASSWORD_MYSQL"),
            "host": os.getenv("HOST_MYSQL"),
            "database": os.getenv("DATABASE_MYSQL"),
        }

        return credentials

    def insert_data_list(self, insert_file, data):
        query_sql = None
        with open(insert_file, "r") as file_sql:
            query_sql = file_sql.read()

        values = []
        for item in data:
            temp_tuple = tuple([i for i in item.values()])
            values.append(temp_tuple)

        print(f"Iniciando inserção de {len(values)} observações")
        self.__cursor.executemany(query_sql, values)
        self.__cnx.commit()
        print(f"Inserção realizada")

    def query_data(self, query_file, parameters=None):
        query_sql = None
        with open(query_file, "r") as file_sql:
            query_sql = file_sql.read()

        tidy_parameters = tuple(parameters)

        self.__cursor.execute(query_sql, tidy_parameters)
        raw_results = self.__cursor.fetchall()

        tidy_results = [item for item in raw_results]
        return tidy_results


if __name__ == "__main__":
    mysql = MySql.instance()
    mock_data = [
        {
            "position": 1,
            "track_name": "DÁKITI",
            "artist_name": "Bad Bunny",
            "streams": 427522,
            "url": "https://open.spotify.com/track/4MzXwWMhyBbmu6hOcLVD49",
            "track_id": "4MzXwWMhyBbmu6hOcLVD49",
            "chart_type": "regional",
            "date": "2020-12-14",
            "period": "daily",
            "region": "ar",
        },
        {
            "position": 2,
            "track_name": "BICHOTA",
            "artist_name": "KAROL G",
            "streams": 376200,
            "url": "https://open.spotify.com/track/7vrJn5hDSXRmdXoR30KgF1",
            "track_id": "7vrJn5hDSXRmdXoR30KgF1",
            "chart_type": "regional",
            "date": "2020-12-14",
            "period": "daily",
            "region": "ar",
        },
        {
            "position": 3,
            "track_name": "Si Me Tomo Una Cerveza",
            "artist_name": "Migrantes",
            "streams": 371049,
            "url": "https://open.spotify.com/track/3lCbsHaN1wCxyDzcNN2x4N",
            "track_id": "3lCbsHaN1wCxyDzcNN2x4N",
            "chart_type": "regional",
            "date": "2020-12-14",
            "period": "daily",
            "region": "ar",
        },
    ]

    # mysql.insert_data_list("../sql/insert_spotify_chart.sql", mock_data)
    parameters = ["2020-12-14", "2020-12-14"]
    res = mysql.query_data("../sql/query_spotify_chart.sql", parameters)

    print(res)
