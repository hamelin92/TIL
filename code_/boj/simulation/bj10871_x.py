import sys
N, X = map(int, sys.stdin.readline().split())
A = filter(lambda x: x < X , map(int, sys.stdin.readline().split()))
print(*A)