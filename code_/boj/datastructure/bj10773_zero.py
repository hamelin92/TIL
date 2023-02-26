import sys

K = int(sys.stdin.readline())
nums = []
for k in range(K):
    n = int(sys.stdin.readline())
    if n:
        nums.append(n)
    else:
        nums.pop()
print(sum(nums))
