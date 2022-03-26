from math import *
def check(number): #단조 증가 수인지 체크하는 함수
    initial = 9
    for _ in range(int(log10(number))+1): # 입력한 수의
        r = number%10
        number = number//10
        if initial >= r:
            initial = r
        else:
            return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N 입력 1 ~ 1000
    A = list(map(int, input().split())) # A의 원소는 총 N개, 1 ~ 30000
    maxnum = -1
    for i in range(N):
        for j in range(i+1, N):
            tmp = A[i]*A[j]
            if check(tmp) == 1 and maxnum < tmp:
                maxnum = tmp

    print(f'#{tc} {maxnum}')

