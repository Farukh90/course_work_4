import json
import os
from abc import ABC, abstractmethod
from src.vacancy_cls import Vacancy
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'vacancies_from_api.json')
filtred_file_path = os.path.join(ROOT_DIR, 'data', 'filtred_vacancies.json')
favorite_file_path = os.path.join(ROOT_DIR, 'data', 'favorite_vacancies.json')

class DataSaver(ABC):
    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass


class JSONSaver(DataSaver):
    def save_file(self, vacancies_list, file_name = file_path):
        '''сохраняет экземпляры вакансий в файл'''
        data_to_save = []
        for vacancy in vacancies_list:
            data_to_save.append(vacancy.__dict__)

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)


    def load_file(self, file_name='vacancies.json'):
        '''Загружает данные из файла JSON'''
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print('файл не найден')

    def get_vacancy_instances_list(self, data: list):
        '''создает список экземпляров вакансий'''
        if data is None:
            return []
        try:
            vacancies_list = []
            for vacancy in data:
                vacancy_inst = Vacancy(**vacancy)
                vacancies_list.append(vacancy_inst)
            return vacancies_list

        except TypeError:
            raise TypeError('количество ключей словаря не соответствуют количеству атрибутов класса вакансия')

