from itertools import combinations

print(sum(max(combinations(
    list(map(int, input().split())),
    3)
)))

