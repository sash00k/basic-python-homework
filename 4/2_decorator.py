def work_time(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


@work_time
def do_work():
    print(fib(100000))


if __name__ == '__main__':
    do_work()
