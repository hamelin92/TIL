import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split())) + [0]
for i in range(1, N):
    numbers[i] += numbers[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(numbers[j-1] - numbers[i-2])