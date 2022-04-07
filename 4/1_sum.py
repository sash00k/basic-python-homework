import sys
sys.setrecursionlimit(1500)


def sum_rec(cur_num=3):
    if cur_num > 1000:
        return 0
    return cur_num + sum_rec(cur_num+1) if cur_num % 3 == 0 or cur_num % 5 == 0 else sum_rec(cur_num+1)


if __name__ == '__main__':
    print(sum_rec())