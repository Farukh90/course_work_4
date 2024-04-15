import requests
from abc import ABC, abstractmethod
from src.vacancy_cls import Vacancy


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass


class HHApi(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str, page_quantity: int = 2):  # page_quantity задаем от 0  до 20
        '''загружает данные c АПИ'''
        self.params['text'] = keyword
        while self.params.get('page') != page_quantity:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
