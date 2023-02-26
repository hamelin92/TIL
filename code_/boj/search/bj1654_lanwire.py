import sys

def divider(length):
    return sum(map(lambda x: x//length, lan))


K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
minimum = 1
maximum = 2147483647
while divider(minimum) >= N and minimum <= maximum:
    medium = (minimum + maximum) // 2
    mid_value = divider(medium)
    if mid_value < N:
        maximum = medium -1
    else:
        minimum = medium + 1
print(medium)
