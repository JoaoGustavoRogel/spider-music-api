import os
import shutil
import unittest
from datetime import datetime

from src.models.SpotifyCrawler import ConcreteFactorySpotifyChartsCrawler


class TestSpotifyCrawler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        factory = ConcreteFactorySpotifyChartsCrawler()

        cls.crawler = factory.create_crawler()
        cls.path = "outputs_spotify"

        try:
            shutil.rmtree(cls.path)
        except Exception:
            pass

        os.mkdir(cls.path)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.path)

    def test_get_data(self):
        extract_data = self.crawler.get_data(
            {
                "start_date": datetime(2020, 12, 12),
                "end_date": datetime(2020, 12, 13),
                "path": self.path,
            }
        )

        self.assertEqual(len(extract_data), 12347)


if __name__ == "__main__":
    unittest.main()
