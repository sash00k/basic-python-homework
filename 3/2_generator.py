# Найдите сумму всех чисел меньше 1000, кратных 3 или 5 с помощью функции генератора


def gen_func():
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            yield i


if __name__ == '__main__':
    print(sum((i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)))

    ans = 0
    for i in gen_func():
        ans += i
    print(ans)
