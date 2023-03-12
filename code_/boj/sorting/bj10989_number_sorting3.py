import sys

N = int(sys.stdin.readline())
num_cnt = [[i, 0] for i in range(10001)]
for i in range(N):
    num_cnt[int(sys.stdin.readline())][1] += 1

for n in filter(lambda x: x[1], num_cnt):
    for k in range(n[1]):
        print(n[0])