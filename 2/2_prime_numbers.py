def get_prime_nums(start: int, end: int) -> list:
    prime_nums = []

    for num in range(start, end+1):
        is_prime = True
        for div in range(2, num // 2 + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)

    return prime_nums


if __name__ == '__main__':
    start, end = map(int, input().split())
    print(get_prime_nums(start=start, end=end))
