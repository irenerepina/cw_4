import requests
from requests import Response

from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_response(self, keyword, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        return requests.get(self.__url, params=self.__params)

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]
