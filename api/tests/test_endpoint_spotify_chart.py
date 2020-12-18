import mock
import os
import shutil
import unittest

from datetime import datetime
from src.models.SpotifyCrawler import ConcreteFactorySpotifyChartsCrawler, ConcreteSpotifyChartsCrawler
from src.routers.endpoints.spotify_chart import get_data_chart


class TestSpotifyChartsRouter(unittest.TestCase):

    @mock.patch("src.models.MySql")
    @mock.patch("src.models.SpotifyCrawler.ConcreteSpotifyChartsCrawler")
    def test_get_data_chart(self, mock_sql, mock_crawler):
        mock_sql().instance.return_value = "instancia criada!"
        mock_crawler().get_data.return_value = "testando o endpoint"
        extract_data = get_data_chart("2020-01-01", "2020-01-10")
        self.assertEqual(extract_data["data"], "testando o endpoint")


if __name__ == "__main__":
    unittest.main()
