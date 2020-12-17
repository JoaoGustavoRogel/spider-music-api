from __future__ import annotations

import concurrent.futures
import json
import spotipy
from datetime import datetime, timedelta
from operator import itemgetter
from spotipy.oauth2 import SpotifyClientCredentials
from src.schemas.Crawler import AbstractCrawler, AbstractFactory

import pandas as pd
import requests

from src.constants import NA, SPOTIFY_API_CLIENT_ID, SPOTIFY_API_CLIENT_SECRET


class ConcreteFactorySpotifyAPICrawler(AbstractFactory):
    def create_crawler(self) -> AbstractCrawler:
        return ConcreteSpotifyAPICrawler()


class ConcreteSpotifyAPICrawler(AbstractCrawler):

    def connect_to_api(self):
        sp = spotipy.Spotify(
            auth_manager = SpotifyClientCredentials(
                client_id = SPOTIFY_API_CLIENT_ID,
                client_secret = SPOTIFY_API_CLIENT_SECRET
            )
        )
        return sp

    def request_data(self, params):

        sp = params["api_object"]
        query = params["query"]
        query_type = params["query_type"]

        print(f"Realizando consulta na api para os seguintes parâmetros:\nquery_type: {query_type}\nid: {query}")

        if query_type == "track_by_id":
            r = sp.track(query)
        elif query_type == "artist_by_id":
            r = sp.artist(query)
        elif query_type == "album_by_id":
            r = sp.album(query)
        elif query_type == "tracks_by_album_id":
            r = sp.album(query)
        elif query_type == "albums_from_artist_id":
            r = sp.artist_albums(query)

        print(f"Exibindo resposta da api: {r}")

        return r


    def process_data(self, data, params):

        def process_track(track_info):
            ret = {}
            ret["track_id"] = track_info["id"]
            ret["track_name"] = track_info["name"]
            ret["track_url"] = track_info["external_urls"]["spotify"]
            ret["track_number"] = track_info["track_number"]
            ret["disc_number"] = track_info["disc_number"]
            ret["duration_ms"] = track_info["duration_ms"]
            ret["artist_id"] = track_info["artists"][0]["id"]
            ret["album_id"] = track_info["album"]["id"]
            ret["popularity"] = track_info["popularity"]
            return ret

        def process_artist(artist_info):
            ret = {}
            ret["artist_id"] = artist_info["id"]
            ret["artist_name"] = artist_info["name"]
            ret["artist_url"] = artist_info["external_urls"]["spotify"]
            ret["followers"] = artist_info["followers"]["total"]
            ret["popularity"] = artist_info["popularity"]
            return ret

        def process_album(album_info):
            ret = {}
            ret["album_id"] = album_info["id"]
            ret["album_name"] = album_info["name"]
            ret["album_url"] = album_info["external_urls"]["spotify"]
            ret["total_tracks"] = album_info["total_tracks"]
            ret["release_date"] = album_info["release_date"]
            ret["artist_id"] = album_info["artists"][0]["id"]
            ret["popularity"] = album_info["popularity"]
            return ret

        tidy = []
        query_type = params["query_type"]

        if query_type == "track_by_id":
            tidy.append(process_track(data))
        
        elif query_type == "artist_by_id":
            tidy.append(process_artist(data))
        
        elif query_type == "album_by_id":
            tidy.append(process_album(data))
        
        elif query_type == "tracks_by_album_id":
            for d in data["tracks"]["items"]:
                track_params = {
                    "query": d["id"],
                    "query_type": "track_by_id",
                    "api_object": params["api_object"]
                }
                tidy.append(process_track(self.request_data(track_params)))

        elif query_type == "albums_from_artist_id":
            for d in data["items"]:
                track_params = {
                    "query": d["id"],
                    "query_type": "album_by_id",
                    "api_object": params["api_object"]
                }
                tidy.append(process_album(self.request_data(track_params)))

        return tidy


    def get_data(self, params):
        sp = self.connect_to_api()
        params["api_object"] = sp
        data = self.request_data(params)
        tidy = self.process_data(data, params)
        print(f"Exibindo dados coletados:\n{tidy}")
        return tidy


"""
# Exemplo do funcionamento
def client_code(factory: AbstractFactory) -> None:
    crwl = factory.create_crawler()
    data = crwl.get_data({
        "query_type": "track_by_id",
        "query": "64EDGnUytmCV7TfOo67810",
        "path": "outputs"
    })
    input()
    data = crwl.get_data({
        "query_type": "artist_by_id",
        "query": "48eO052eSDcn8aTxiv6QaG",
        "path": "outputs"
    })
    input()
    data = crwl.get_data({
        "query_type": "album_by_id",
        "query": "5Dq6jkYO5H7KzxXSazhLxs",
        "path": "outputs"
    })
    input()
    data = crwl.get_data({
        "query_type": "tracks_by_album_id",
        "query": "5Dq6jkYO5H7KzxXSazhLxs",
        "path": "outputs"
    })
    input()
    data = crwl.get_data({
        "query_type": "albums_from_artist_id",
        "query": "48eO052eSDcn8aTxiv6QaG",
        "path": "outputs"
    })


if __name__ == "__main__":
    print("Testando o crawler via api")
    client_code(ConcreteFactorySpotifyAPICrawler())
"""