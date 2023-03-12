import sys

N = int(sys.stdin.readline())
nums = [None]*N
print(*sorted(int(sys.stdin.readline()) for _ in range(N)), sep="\n")
