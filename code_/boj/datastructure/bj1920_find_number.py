import sys

def search(b, l):
    global N
    r = N-1
    while l < r:
        mid = (l+r)//2
        if A[mid] > b:
            r = mid-1
        elif A[mid] < b:
            l = mid + 1
        else:
            return 1
    if A[l] == b:
        return 1
    return 0


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
for b in B:
    print(search(b, 0))
