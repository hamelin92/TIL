from math import gcd

N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    T, A, B = map(int, input().split())
    if T > 0:
        nums[A-1:B] = [nums[k]+T for k in range(A-1,B)]
    else:
        d = nums[A-1]
        for n in range(A-1,B-1):
            d = gcd(d, nums[n+1])
            if d == 1:
                break
        print(d)

