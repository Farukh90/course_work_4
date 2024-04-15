from src.vacancy_cls import Vacancy


class VacanciesParser():
    """
    Класс для парсинга данных с АПИ
    """

    def parser_api_vacancies(self, api_data: list):
        '''парсит данные c апи по определенным критериям'''
        vacancies_list = []

        for data in api_data:
            name = data.get('name')
            salary = data.get('salary')
            if salary and salary.get('from'):
                filtered_salary = salary['from']
            else:
                filtered_salary = 0
            snippet = data.get('snippet')
            if salary:
                salary = data.get('salary')
                currency = salary.get('currency')
            else:
                currency = ''
            requirement = snippet.get('requirement')
            if requirement:
                requirement = requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            else:
                requirement = 'нет требований'
            vacancy_url = data.get('alternate_url')
            area = data.get('area')
            region = area.get('name')

            id_number = data.get('id')
            vacancy_instance = Vacancy(id_number, region, name, filtered_salary, currency, requirement, vacancy_url)

            vacancies_list.append(vacancy_instance)
        return vacancies_list
