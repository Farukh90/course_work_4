
red_col = '\033[91m'
rest_red_col = '\033[0m'
class DataManager():
    def __init__(self, json_saver):
        self.json_saver = json_saver

    '''реализованы методы для сортировки, фильтрации, добавления, удаления объектов вакансий'''


    def filter_by_area(self, vacancies_list, region_name: str):
        '''фильтрует по региону'''
        catched = 0
        filtred_vacancies = []
        for vacancy in vacancies_list:
            if vacancy.region == region_name:
                filtred_vacancies.append(vacancy)
                catched += 1
        if catched != 0:
            print(f"{red_col}количество совпадений {catched}{rest_red_col}")
            return filtred_vacancies
        else:
            print(f"{red_col}совпадение по региону '{region_name}' не найдено, сбрось фильтр!{rest_red_col}")
            return filtred_vacancies

    def filter_by_currency(self, vacancies_list, currency: str):
        '''фильтрует по валюте'''
        catched = 0
        filtred_by_currency = []
        for vacancy in vacancies_list:
            if vacancy.currency is not None and vacancy.currency == currency:
                filtred_by_currency.append(vacancy)
                catched += 1
        if catched != 0:
            print(f"{red_col}количество совпадений {catched}{rest_red_col}")
            return filtred_by_currency
        else:
            print(f"{red_col}валюта '{currency}' не найдена, сбрось фильтр!{rest_red_col}")
            return filtred_by_currency

    def sort_by_salary(self, vacancies_list):
        '''сортирует по зарплате'''
        return sorted(vacancies_list, reverse=True)

    def get_sorted_top_10(self, vacancies_list, quantity: int = 10):
        '''возвращает топ 10 вакансий по убыванию зарплаты'''
        sorted_vacancies = sorted(vacancies_list, reverse=True)
        return sorted_vacancies[:quantity]

    def filter_by_salary_range(self, vacancies_list, salary_min: int, salary_max: int):
        '''фильтрует по диапазону зарплат'''
        catched = 0
        filtred_list = []
        for vacancy in vacancies_list:
            if salary_min <= vacancy.salary <= salary_max:
                filtred_list.append(vacancy)
                catched += 1
        if catched != 0:
            print(f"{red_col}количество совпадений {catched}{rest_red_col}")
            return filtred_list
        else:
            print(f"{red_col}зарплаты в диапазоне '{salary_min}' - '{salary_max}' отсутствуют, сбрось фильтр!{rest_red_col}")
            return filtred_list

    def add_vacancy(self, vacancies_list, vacancy_instance):
        '''добавляет экземпляр вакансии в список экземпляров вакансий'''
        if vacancy_instance in vacancies_list:
            print(f"{red_col}Вакансия '{vacancy_instance}' уже существует.{rest_red_col}")
        else:
            vacancies_list.append(vacancy_instance)
            print(f"{red_col} '{vacancy_instance}' Вакансия добавлена.{rest_red_col}")
        return vacancies_list

    def add_favorite_vacancy_by_id(self, vacancies_list, vacancy_id):
        '''добавляет экземпляр вакансии в список избранных экземпляров вакансий'''
        new_list = []
        for vacancy in vacancies_list:
            if vacancy_id == vacancy.id_:
                new_list.append(vacancy)
                print(f"{red_col} Вакансия с айди '{vacancy.id_}'  добавлена в избранное.{rest_red_col}")
                break
        return new_list

    def del_vacancy_by_id(self, vacancies_list, id_number):
        '''удаляет экземпляр вакансии по id'''
        new_vacancies_list = [vacancy for vacancy in vacancies_list if vacancy.id_ != id_number]
        if len(new_vacancies_list) == len(vacancies_list):
            print(f"{red_col}Вакансия с id '{id_number}' не найдена.{rest_red_col}")
        else:
            print(f"{red_col}Вакансия с id '{id_number}' удалена.{rest_red_col}")
        return new_vacancies_list