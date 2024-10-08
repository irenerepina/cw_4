from abc import ABC, abstractmethod
import json


class Saver(ABC):
    """ Абстрактный класс для записи в файл """
    def __init__(self, filename=None):
        self.__filename = filename

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONSaver(Saver):
    """ Класс для записи в json-файл """

    def __init__(self, filename):
        """ Конструктор класса """

        super().__init__(filename)

    def write_data(self, vacancies):
        """ Запись данных в json """

        data = self.get_data()
        data.extend(vacancies)

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """ Получение данных json """

        try:
            return json.load(open(self.__filename))
        except FileNotFoundError:
            return []

    def del_data(self):
        """ Удаление данных из файла """

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
