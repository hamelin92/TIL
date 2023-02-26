import sys

def binary_search(left, right, t):
    while left <= right:
        mid = (left+right)//2
        if dpl[mid] < t <= dpl[mid+1]:
            return mid
        elif dpl[mid] >= t:
            right = mid -1
        else:
            left = mid + 1
    return mid

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1]*N
dpl = [-1000000001]
for i in range(N):
    if A[i] > dpl[-1]:
        dp[i] = len(dpl)
        dpl.append(A[i])
    else:
        l = binary_search(0, len(dpl)-1, A[i])
        if dpl[l] < A[i] <= dpl[l+1]:
            dpl[l+1] = A[i]
            dp[i] = l+1
print(dp, dpl)