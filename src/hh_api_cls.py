from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass
