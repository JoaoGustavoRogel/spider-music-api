import os
import shutil
import unittest

from datetime import datetime
from src.models.SpotifyAPICrawler import ConcreteFactorySpotifyAPICrawler


class TestSpotifyAPICrawler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        factory = ConcreteFactorySpotifyAPICrawler()

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
        extract_data = self.crawler.get_data({
            "query_type": "tracks_by_album_id",
            "query": "5Dq6jkYO5H7KzxXSazhLxs",
            "path": self.path,
        })

        self.assertEqual(len(extract_data), 21)

if __name__ == "__main__":
    unittest.main()