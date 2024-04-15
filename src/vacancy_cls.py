class Vacancy():
    '''Класс для организации данных по вакансиям в удобном виде. хранит в себе полезные атрибуты по вакансиям'''

    def __init__(self, id_, region, name, salary, currency, requirement, vacancy_url):
        self.id_ = id_
        self.region = region
        self.name = name
        self.salary = salary
        self.currency = currency
        self.requirement = requirement
        self.vacancy_url = vacancy_url

    def __str__(self):
        cut_line = '-' * 120
        return f'''{cut_line}

id:{self.id_}, Регион: {self.region}, Вакансия: {self.name}, Зарплата: {self.salary} {self.currency}, 
Требования: {self.requirement})
ссылка на вакансию: {self.vacancy_url}
'''

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __lt__(self, other):
        if self.salary is not None and other.salary is not None:
            return self.salary < other.salary
