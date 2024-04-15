from abc import ABC, abstractmethod


class DataSaver(ABC):
    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass

