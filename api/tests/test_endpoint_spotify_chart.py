import mock
import os
import shutil
import unittest

from datetime import datetime
from src.models.SpotifyCrawler import ConcreteFactorySpotifyChartsCrawler, ConcreteSpotifyChartsCrawler
from src.routers.endpoints import spotify_chart


class TestSpotifyChartsRouter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_mysql = mock.patch.object(spotify_chart, "mysql_db", return_value = "instancia_criada")

    @mock.patch("src.models.SpotifyCrawler.ConcreteSpotifyChartsCrawler")
    def test_get_data_chart(self, mock_crawler):
        mock_crawler().get_data.return_value = "testando o endpoint"
        extract_data = spotify_chart.get_data_chart("2020-01-01", "2020-01-10")
        self.assertEqual(extract_data["data"], "testando o endpoint")


if __name__ == "__main__":
    unittest.main()
