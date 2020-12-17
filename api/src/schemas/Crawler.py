import os
import shutil
from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def get_data(self, params):
        pass

    @abstractmethod
    def process_data(self, data, params):
        pass

    @abstractmethod
    def request_data(self, params):
        pass

    def clear_folder(self, path):
        shutil.rmtree(path)
        os.mkdir(path)


class AbstractFactory(ABC):
    @abstractmethod
    def create_crawler(self) -> AbstractCrawler:
        pass
