import os
import time

from src.hh_api_cls import HHApi
from src.vacancies_parser_cls import VacanciesParser
from src.data_manager_cls import DataManager
from src.file_manager_cls import JSONSaver
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'vacancies_from_api.json') #название файла по умолчанию
filtred_file_path = os.path.join(ROOT_DIR, 'data', 'filtred_vacancies.json') #название файла с результатом фильтрации
favorite_file_path = os.path.join(ROOT_DIR, 'data', 'favorite_vacancies.json') #название файла избранных вакансий

def main():
    hh_api_instance = HHApi()
    parser_instance = VacanciesParser()
    json_saver_instance = JSONSaver()
    data_manager_instance = DataManager(json_saver_instance)

    key_word = input('Введите поисковый запрос: ')
    page_quantity = input('Введите количество запрашиваемых страниц от 1 до 20: ')
    if page_quantity and 0 < int(page_quantity) <=20:
        hh_api_instance.load_vacancies(key_word, int(page_quantity)) #запрос через апи
    else:
        print('вы ввели неверное число, по умолчанию будет загружено 2 страницы')
        time.sleep(2)
        hh_api_instance.load_vacancies(key_word) #запрос через апи
    vacancies_list_from_api = hh_api_instance.vacancies #получаем список словарей вакансий которые пришли с апи
    parsed_vacancies_list = parser_instance.parser_api_vacancies(vacancies_list_from_api) #парсим вакансии в ЭК вакансия

    save_file = data_manager_instance.json_saver.save_file(parsed_vacancies_list) #сохраняем данные в JSON
    loaded_file = data_manager_instance.json_saver.load_file(file_path) #загружаем данные из JSON
    loaded_vacancies_list_from_file = data_manager_instance.json_saver.get_vacancy_instances_list(loaded_file) #создаем ЭК вакансий

    #для взаимодействия с пользователем
    save_file_for_user_interact = data_manager_instance.json_saver.save_file(parsed_vacancies_list,filtred_file_path)#сохраняем данные в JSON
    load_file_for_user_interact = data_manager_instance.json_saver.load_file(filtred_file_path)  #загружаем данные из JSON
    vacancies_for_user_interact = data_manager_instance.json_saver.get_vacancy_instances_list(load_file_for_user_interact) #создаем ЭК вакансий
    list(map(print, vacancies_for_user_interact)) #выводим вакансии полученные с АПИ
    favorite_list = data_manager_instance.json_saver.load_file(favorite_file_path) #заводим отдельный список для фильтрации пользователя
    favorite_vacancies = data_manager_instance.json_saver.get_vacancy_instances_list(favorite_list) #создаем ЭК вакансий
    while True:

        print('''1 - для сортировки по региону
2  - сортировка по убыванию зарплат
3  - фильтрация по валюте
4  - фильтрация по диапазону зарплат
5  - вывод топ 10 по зарплате
6  - добавить в избранное (по ID)
7  - вывод избранных вакансий на экран
8  - удалить из избранного (по ID)
9  - удаление вакансии (по ID)
10 - сбросить фильтры
0  - завершение программы''')
        choice_number = ['1','2','3','4','5','6','7','8','9','10','0']
        user_choice = input(f"{'⛔'*110}\nВведите номер и нажмите 'enter' для пуска действия: ")

        if user_choice and user_choice == '1' and user_choice in choice_number: #для сортировки по региону
            filter_word_by_area = input('Введите регион: ').title()
            vacancies_for_user_interact = data_manager_instance.filter_by_area(vacancies_for_user_interact, filter_word_by_area)
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '2' and user_choice in choice_number: #сортировка по убыванию зарплат
            vacancies_for_user_interact = data_manager_instance.sort_by_salary(vacancies_for_user_interact)
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '3' and user_choice in choice_number: #фильтрация по валюте
            filter_word = input('Введите валюту: ').upper()
            vacancies_for_user_interact = data_manager_instance.filter_by_currency(vacancies_for_user_interact, filter_word)
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '4' and user_choice in choice_number:  # фильтрация по диапазону зарплат
            salary_range = input('введите диапазон зарплат через пробел: ')
            splited_input = salary_range.split(' ')
            min_ = int(splited_input[0])
            max_ = int(splited_input[1])
            print(max_)
            vacancies_for_user_interact = data_manager_instance.filter_by_salary_range(vacancies_for_user_interact, min_, max_)
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '5' and user_choice in choice_number: #вывод топ 10 по зарплате
            vacancies_for_user_interact = data_manager_instance.get_sorted_top_10(vacancies_for_user_interact, 10)
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '6' and user_choice in choice_number: #добавить в избранное (по ID)
            vacancy_id = str(input('Введите ID вакансии: '))
            favorite_vacancies += data_manager_instance.add_favorite_vacancy_by_id(vacancies_for_user_interact, vacancy_id)

        elif user_choice and user_choice == '7' and user_choice in choice_number: #вывод избранных вакансий на экран
            list(map(print, favorite_vacancies))

        elif user_choice and user_choice == '8' and user_choice in choice_number: #удалить из избранного (по ID)
            vacancy_id = str(input('Введите ID вакансии: '))
            favorite_vacancies = data_manager_instance.del_vacancy_by_id(favorite_vacancies,vacancy_id)

        elif user_choice and user_choice == '9' and user_choice in choice_number: #удаление вакансии (по ID)
            vacancy_id = str(input('Введите ID вакансии: '))
            vacancies_for_user_interact = data_manager_instance.del_vacancy_by_id(vacancies_for_user_interact, vacancy_id)

        elif user_choice and user_choice == '10' and user_choice in choice_number: #сбросить фильтры
            vacancies_for_user_interact = loaded_vacancies_list_from_file
            list(map(print, vacancies_for_user_interact))

        elif user_choice and user_choice == '0' and user_choice in choice_number: #завершение программы
            data_manager_instance.json_saver.save_file(vacancies_for_user_interact, filtred_file_path)
            break

        else:
            print('введите номер!')
            continue

        try:
            data_manager_instance.json_saver.save_file(favorite_vacancies, favorite_file_path)

        except NameError as e:
            print(f"Не удалось сохранить избранные вакансии. ошибка: {e}")


if __name__ == "__main__":
    main()