#실패
#N = int(input())
#polys = [list(map(int, input().split())) for _ in range(N)]
#polys.sort()
#l_max = 0
#r_max = 0
#l_idx = 0
#l_area = 0
#r_area = 0
#result = 0
#idx = 0
#while N >= 3:
#    if polys[idx][1] > l_max:
#        l_area += polys[idx][1] * (polys[idx+1][0] - polys[idx][0])
#        print(f'{polys[idx][1] * (polys[idx+1][0] - polys[idx][0])} 더해짐')
#        l_max = polys[idx][1]
#    else:
#        l_area += l_max * (polys[idx+1][0] - polys[idx][0])
#        print(f'{l_max * (polys[idx+1][0] - polys[idx][0])} 더해짐')
#    if polys[N-1+idx][1] > r_max:
#        r_area += polys[N-1+idx][1] * (polys[N-1+idx][0] - polys[N-1+idx-1][0])
#        r_max = polys[N-1+idx][1]
#        print(f'{polys[N-1+idx][1] * (polys[N-1+idx][0] - polys[N-1+idx-1][0])} 더해짐')
#    else:
#        r_area += r_max * (polys[N-1+idx][0] - polys[N-1+idx-1][0])
#        print(f'{r_max * (polys[N-1+idx][0] - polys[N-1+idx-1][0])} 더해짐')
#    idx += 1
#    N = N-2
#if N == 2:
#    l_max, r_max = max(polys[idx][1], min(l_max, r_max)), max(polys[idx+1][1], min(l_max, r_max))
#    print(l_area+r_area)
#    print(l_max, r_max)
##    r_max = max(polys[idx+1][1], min(l_max, r_max))
#    result += min(l_max, r_max) * (polys[idx+1][0] - polys[idx][0]) + max(l_max, r_max)
#elif N == 1:
#    result += max([polys[idx+N//2][1], min(l_max, r_max)])
#print(result + l_area + r_area)


#입력 ( 처음 숫자 N을 따로 받고 그이후로 나오는 정보들은 리스트로 저장 )
N = int(input())
polys = [list(map(int, input().split())) for _ in range(N)]

#입력받은 값 리스트를 정렬( x좌표 기준으로 정렬하는 것과 같다.)
polys.sort()

#x좌표값과 높이값들을 따로 분리
N_x, heights = zip(*polys)

#막대 중 가장 높은 값에 해당하는, 즉 heights 중에서 최대값을 변수로 저장.
max_h = max(heights)

#왼쪽 기준으로  계산하기 위한 초기값
l_max = heights[0]
l_area = 0
l_idx = 0

#오른쪽 기준으로 계산하기 위한 초기값
r_max = heights[N-1]
r_area = 0
r_idx = N-1

#왼쪽,오른쪽 기준으로 각각 최대 높이에 도달하기 전까지 넓이 계산
#왼쪽은 맨 왼쪽부터 오른쪽방향으로, 오른쪽은 맨 오른쪽부터 왼쪽방향으로
#만약 진행방향에 기존 값보다 큰 값이 있다면 그 사이에
#더 작은 값이 있더라도 묻히게 된다.
#즉, 앞서 구한 최대값을 기준으로 진행방향에 따라 갱신되는 더 큰 높이로
#천장을 덮어주면 된다.
while heights[l_idx] < max_h:
    if heights[l_idx] > l_max:
        l_area += heights[l_idx] * (N_x[l_idx+1] - N_x[l_idx])
        l_max = heights[l_idx]
    else:
        l_area += l_max * (N_x[l_idx+1] - N_x[l_idx])
    l_idx += 1
while heights[r_idx] < max_h:
    if heights[r_idx] > r_max:
        r_area += heights[r_idx] * (N_x[r_idx] - N_x[r_idx-1])
        r_max = heights[r_idx]
    else:
        r_area += r_max * (N_x[r_idx] - N_x[r_idx-1])
    r_idx -= 1

#앞선 while문에서 최대높이에 도달할때부터 계산을 하지 않았기에
#최대값에 해당하는 기둥이 받치고 있는 공간의 넓이를 계산
#최대값보다 더 큰 높이를 가진 기둥은 존재하지 않으므로
#최대값을 가진 기둥들 사이의 공간은 최대값과 같은 높이로 설정하면 된다.
mid_val = max_h * (N_x[r_idx] - N_x[l_idx]+1)

#각각 구해진 왼쪽 넓이 오른쪽 넓이 중간넓이를 모두 더해서 출력한다.
print(mid_val + l_area + r_area)

'''
10
1 10
3 9
5 8
7 7
9 6
11 5
13 4
15 3
17 2
19 1
'''