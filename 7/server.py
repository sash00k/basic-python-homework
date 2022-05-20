from copy import deepcopy
from my_errors import *
import csv


class MyServer:

    def __init__(self, db_name: str, routes: dict, private_routes: set):
        self.name = db_name
        self.__routes = deepcopy(routes)
        self.__private_routes = private_routes # при обращении к приватным путям будет подниматься ошибка с кодом 500

    def check_permission(self, path):
        if path in self.__private_routes:
            raise PermissionsError

    def read_file(self, path: str) -> list:
        with open(self.name + '_' + path[1:] + '.csv', 'r') as file:
            raw_info = csv.reader(file)
            headers = next(raw_info)
            info = [{header: row[i] for header, i in zip(headers, range(len(headers)))} for row in raw_info]

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
        except PermissionsError as err:
            body = None
            code = err.code
            status = 'KO'
        return {'status': status,
                'code': code,
                'body': body}

    def post(self, path: str, new_info: list) -> dict:
    # этот метод релизован только для случая добавления новой строки в табличку, где все остортировано по STUDENT_ID
    # ясно, что запрос на добавление, например, оценок, работал бы иначе, ну он и принимал бы другой набор данных
        try:
            self.check_permission(path=path)
            if path not in self.__routes['POST']:
                raise FileNotFoundError
            with open(self.name + '_' + path[1:] + '.csv', 'a') as file:
                # у нас такая простенькая база данных, что в каждой таблице ключевое значения - 'STUDENT_ID'
                # так что поэтому оно тут так явно и прописано
                index = int(self.read_file(path=path)[-1]['STUDENT_ID']) + 1
                file_writer = csv.writer(file)
                file_writer.writerow([index]+new_info)
            code = 200
            status = 'OK'
        except FileNotFoundError:
            body = None
            code = 404
            status = 'KO'
        except PermissionsError as err:
            body = None
            code = err.code
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
    print(server.get(path='/grades'))
    print(server.get(path='/schedule'))
    print(server.post(path='/students', new_info=['Бочкарев Алекcандр Дмитриевич']))
    print()

    # incorrect requests
    print(server.get(path='/invalid_path'))
    print(server.get(path='/passwords'))
    print(server.post(path='/payments', new_info=['Бочкарев Алекcандр Дмитриевич']))


