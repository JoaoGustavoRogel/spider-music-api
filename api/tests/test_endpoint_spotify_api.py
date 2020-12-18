import mock
import os
import shutil
import unittest

from datetime import datetime
from src.models.SpotifyAPICrawler import ConcreteFactorySpotifyAPICrawler, ConcreteSpotifyAPICrawler
from src.routers.endpoints import spotify_api


class TestSpotifyAPIRouter(unittest.TestCase):
    @mock.patch("src.models.SpotifyAPICrawler.ConcreteSpotifyAPICrawler")
    def test_get_data_chart(self, mock_crawler):
        mock_crawler().get_data.return_value = "testando o endpoint"
        extract_data = spotify_api.query_crawler_track_by_id("random_id")
        self.assertEqual(extract_data["data"], "testando o endpoint")


if __name__ == "__main__":
    unittest.main()
