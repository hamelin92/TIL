import sys

N, M = map(int, sys.stdin.readline().split())
memo = dict()
for i in range(N):
    site, pw = sys.stdin.readline().split()
    memo[site] = pw
for i in range(M):
    print(memo[sys.stdin.readline().strip("\n")])