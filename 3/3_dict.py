# Запишите в словарь по ключам от 1 до 10, список чисел от 0 до 1000, которые делятся на соответствующие ключи


def get_dividers_dict():
    # тут list, а не tuple, чтоб принтом выводились значения, а не просто тип и адрес кортежа
    voc = {i: [j for j in range(1001) if j % i == 0] for i in range(1, 11)}
    return voc


if __name__ == '__main__':
    print(get_dividers_dict())
