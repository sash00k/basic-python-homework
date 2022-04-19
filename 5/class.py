# Напишите класс Building
# Необходимые атрибуты класса: дверь (состояние open/closed) (Может быть отдельным объектом), адрес, площадь
# Класс должен иметь методы open_door, close_door
# * Напишите два класса-наследника Building.
# В первом классе добавьте атрибут со списком окон и возможностью их закрывать/открывать
# Второй придумайте сами и добавьте к нему два любых метода
# **
# 1. Добавьте в классы возможность вывода через print({Building})) в формате
# "{Тип строения} по адресу {адрес}. Дверь {открыта/закрыта}"
# 2. Добавьте логику сложения двух строений. (Достаточно если будет реализовано только для двух строений одного и того же типа, для двух разных типов по желанию)
# Итогом сложения должен быть объект по адресу строения с наибольшей площадью из слагаемых, с площадью равной суммарной площади двух строений
# И дверь должна быть открыта если хотя бы одно из исходных строений было с открытой дверью

class Building:

    def __init__(self, address, area=None, is_opened=True):
        self.address = address
        self.area = area
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

    def __add__(self, other):
        return Building(address = max((self, other), key = lambda x: x.area).address,
                        area = self.area + other.area,
                        is_opened = self.is_opened or other.is_opened)

    def __str__(self):
        return f'Строение по адресу {self.address}. Дверь ' + ('открыта.' if self.is_opened else 'закрыта.')


class School(Building):

    def __init__(self, address=None, area=None, is_opened=True, windows=None):
        self.windows = windows
        Building.__init__(self, address = address, area=area, is_opened=is_opened)

    def __add__(self, other):
        #не знаю, что тут лучше было: использовать наследованный метод, или скопипастить его содержимое сюда (то же с кафе)
        result = Building.__add__(self, other)
        return School(address = result.address,
                      area = result.area,
                      is_opened = result.is_opened,
                      windows = self.windows + other.windows)

    def __str__(self):
        return f'Школа по адресу {self.address}. Дверь ' + ('открыта.' if self.is_opened else 'закрыта.')

    def windows_info(self):
        for i, is_window_opened in zip(range(len(self.windows)), self.windows):
            print(f'{i} окно ' + ('открыто' if is_window_opened else 'закрыто'))

    def open_window(self, i: int):
        self.windows[i] = True

    def close_window(self, i: int):
        self.windows[i] = False


class Cafe(Building):

    def __init__(self, address=None, area=None, is_opened=True, need_qr: bool = None, tables=None):
        self.need_qr = need_qr
        self.tables = tables
        Building.__init__(self, address = address, area=area, is_opened=is_opened)

    def __add__(self, other):
        result = Building.__add__(self, other)
        return Cafe(address = result.address,
                    area = result.area,
                    is_opened = result.is_opened,
                    need_qr = self.need_qr and other.need_qr,
                    tables = self.tables + other.tables)

    def __str__(self):
        return f'Кафе по адресу {self.address}. Дверь ' + ('открыта. ' if self.is_opened else 'закрыта. ') + \
               ('QR нужен.' if self.need_qr else 'QR не нужен.') + \
               f' {sum(map(int, self.tables))}/{len(self.tables)} столиков свободно.'

    def tables_info(self):
        for i, is_table_free in zip(range(len(self.tables)), self.tables):
            print(f'{i} столик ' + ('свободен' if is_table_free else 'занят'))


if __name__ == '__main__':
    dom_1 = Building(address='Зорге 71', area=36, is_opened=False)
    dom_2 = Building(address='Громова 39', area=70, is_opened=True)
    school = School(address='Пирогова 1', area=734, is_opened=True, windows=[False, True, False])
    cafe = Cafe(address='Ильича 15', area=110, is_opened=True, need_qr=True, tables=[True, False, False, True])

    print(dom_1)
    print(dom_2)
    print(dom_1 + dom_2)
    print()

    print(school)
    school.windows_info()
    print()

    print(cafe)
    cafe.tables_info()
