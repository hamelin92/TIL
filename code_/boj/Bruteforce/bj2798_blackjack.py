from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_val = 0
for e in combinations(cards, 3):
    v = sum(e)
    if max_val < v <= M:
        max_val = v
        if max_val == M:
            break
print(max_val)