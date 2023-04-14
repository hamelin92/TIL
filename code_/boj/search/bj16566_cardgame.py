import sys

N, M, K = map(int, sys.stdin.readline().split())
blues = list(map(int, sys.stdin.readline().split()))
reds = list(map(int, sys.stdin.readline().split()))
count = [0]*4000001
sorted_blue = []
max_num = 0
for num in blues:
    count[num] = 1
    if num > max_num:
        max_num = num
for num in range(max_num+1):
    if count[num]:
        sorted_blue.append(num)

def binary_search(sarr, k):
    # sarr: 탐색 인덱스 범위 배열
    # 게임 횟수 k
    return

