# Реализуйте класс, который будет вести себя как сервер
# Класс должен принимать запросы GET, POST
# При инициализации должны быть прописаны допустимые пути
# При запросе на не существующий путь, класс должен отдавать ошибку 404
# В обработчиках запросов должны присутствовать блоки try/except и при возникновении ошибки при обработке, необходимо отдавать 500 ошибку
#
# В ответ на запросы должны возвращаться словари со следующей структурой:
# {
#     'status': 'OK',  # 'KO' В случае ошибки
#     'code': 200,  # 404, 500 и тд в зависимости от ошибки
#     'body': None,  # Тело ответа если предполагается запросом в произвольной форме
# }
#
# Обязательные к реализации пути:
# 1. GET '/students' - должен возвращаться список имен (возможно дополнительную информацию)
# взятых из файла (почти база данных) (заполните файл сами)
# 2. POST '/students' - должен дозаписывать в файл имя
# 3. Любой путь, который должен поднимать (raise) 500 ошибку при обращении к нему (опишите как её получить в комментарии)
# 4. Добавьте один путь на ваш выбор
#
# Пример обращения к вашему серверу:
# =============================================
# server = YourServer(routes={'GET': ['/students', '/grades', '/schedule'], 'POST': ['/students']})
# server.get(path='/students')
# >> {'status': OK, 'code': 200, 'body': [{имена взятые из файла}]}
# server.post(path='/students', body={'name': 'Guido van Rossum'}) # Записываем 'Guido van Rossum' в файл
#
# server.get(path='/students')
# >> {'status': OK, 'code': 200, 'body': [{имена взятые из файла + 'Guido van Rossum'}]}
#
# server.get(path='/invalid_path')
# >> {'status': KO, 'code': 404, 'body': None}
# =============================================
# Примеры сверху нужны только для примерного понимания как это должно выглядеть, у вас есть право изменять их по своему выбору
# Но конечная реализация должна соответствовать всем требованиям

from copy import deepcopy
from my_errors import *
import csv


class MyServer:

    def __init__(self, routes: dict):
        self.routes = deepcopy(routes)

    @staticmethod
    def read_file(path: str) -> list | None:
        try:
            with open(path[1:] + '.csv', 'r') as file:
                raw_info = csv.reader(file)
                info = [{'STUDENT_ID': row[0], 'NAME': row[1]} for row in raw_info]
                # return_dict = {'STUDENT_ID': [row[0] for row in info], 'NAME': [row[1] for row in info]}

        except FileNotFoundError:
            info = None
            raise Error404
        except Exception:
            info = None
            raise Error500
        except BaseException:
            info = None
            raise Error666

        return info

    def get(self, path: str) -> dict:
        try:
            body = self.read_file(path=path)
            code = 200
            status = 'OK'
        except MyException as err:
            status = 'KO'
            code = err.code
        return {'status': status,
                'code': code,
                'body': body}


if __name__ == '__main__':
    server = MyServer(routes={'GET': ['/students', '/grades', '/schedule'], 'POST': ['/students']})
    print(server.get(path='/staudents'))
