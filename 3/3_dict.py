def get_dividers_dict():
    # тут list, а не tuple, чтоб принтом выводились значения, а не просто тип и адрес кортежа
    voc = {i: [j for j in range(1001) if j % i == 0] for i in range(1, 11)}
    return voc


if __name__ == '__main__':
    print(get_dividers_dict())
