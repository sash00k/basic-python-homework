# фактически тут все методы реализованы только для запросов в '/students'
# в целом понятно, как их сделать более общими, надо в .csv файлы тогда писать названия столбцов
# ну и тогда надо генерировать словари иначе: по первой считанной строке ключи, а по последующим - значения
# но я че-то уже не стал доделывать

from copy import deepcopy
from my_errors import *
import csv


class MyServer:

    def __init__(self, db_name: str, routes: dict, private_routes: set):
        self.name = db_name
        self.routes = deepcopy(routes)
        self.private_routes = private_routes # при обращении к приватным путям будет подниматься ошибка с кодом 500

    def check_permission(self, path):
        if path in self.private_routes:
            raise PermissionsError

    def read_file(self, path: str) -> list:
        with open(self.name + '_' + path[1:] + '.csv', 'r') as file:
            raw_info = csv.reader(file)
            info = [{'STUDENT_ID': row[0], 'NAME': row[1]} for row in raw_info]

        return info

    def get(self, path: str) -> dict:
        try:
            self.check_permission(path=path)
            body = self.read_file(path=path)
            code = 200
            status = 'OK'
        except FileNotFoundError:
            body = None
            code = 404
            status = 'KO'
        except PermissionsError:
            body = None
            code = 500
            status = 'KO'
        return {'status': status,
                'code': code,
                'body': body}

    def post(self, path: str, new_name: str) -> dict:
        try:
            self.check_permission(path=path)
            if path not in self.routes['POST']:
                raise FileNotFoundError
            with open(self.name + '_' + path[1:] + '.csv', 'a') as file:
                index = int(self.read_file(path=path)[-1]['STUDENT_ID']) + 1
                file_writer = csv.writer(file)
                file_writer.writerow([index, new_name])
            code = 200
            status = 'OK'
        except FileNotFoundError:
            body = None
            code = 404
            status = 'KO'
        except PermissionsError:
            body = None
            code = 500
            status = 'KO'
        return {'status': status,
                'code': code}


if __name__ == '__main__':
    server = MyServer(db_name='MyDatabase',

                      routes={'GET': {'/students', '/grades', '/schedule', '/passwords', '/payments'},
                              'POST': {'/students'}},
                      private_routes={'/passwords', '/payments'})

    # correct requests
    print(server.get(path='/students'))
    print(server.post(path='/students', new_name='Бочкарев Алекcандр Дмитриевич'))
    print()

    # incorrect requests
    print(server.get(path='/invalid_path'))
    print(server.get(path='/passwords'))
    print(server.post(path='/payments', new_name='Бочкарев Алекcандр Дмитриевич'))

