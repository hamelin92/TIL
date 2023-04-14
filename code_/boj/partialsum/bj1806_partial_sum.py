import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sums = [0] + numbers
for i in range(1, N+1):
    sums[i] += sums[i-1]
start = end = 0
val = 0
min_len = N+2
while end < N+1:
    val = sums[end] - sums[start]
    if val < S:
        end += 1
    else:
        if end-start < min_len:
            min_len = end-start
        start += 1
if min_len > N+1:
    print(0)
else:
    print(min_len)