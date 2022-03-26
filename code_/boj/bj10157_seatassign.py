#for idx1 in range(1,11):
#    for idx2 in range(1,11):
#        for k in range(1, idx1*idx2+1):
C, R = map(int, input().split())
#C, R = idx1, idx2
K = int(input())
#K = k
'''
if K > 1000000:
    print(0)
elif K > C*R:
    print(0)
else:
    #i=0
    if C==R and K > C*R-4 and C%2 == 0: # 짝수 케이스
        rcp = K-C*R +4
        if rcp == 1:
            print(f'{C//2} {C//2}')
        elif rcp == 2:
            print(f'{C//2} {C//2+1}')
        elif rcp == 3:
            print(f'{C//2+1} {C//2+1}')
        else:
            print(f'{C//2+1} {C//2}')
    else:
        i = int(((C+R)-((C+R)**2 -4*K)**(1/2))/4)
        
        while K > 2*(C+R-2) and C >2 and R > 2:
            K -= 2*(C+R-2)
            C -= 2
            R -= 2
            i += 1
        
        K = K - 2*(C+R)*i + 4*i**2
        C -= 2*i
        R -= 2*i
        if K <R:
            result = [1, K]
        elif K < C+R-1:
            result = [K-R+1, R]
        elif K < C+2*R-2:
            result = [C, R-(K-C-R+1)]
        else:
            result = [C-(K-C-2*R+2), 1]
        result[0] += i
        result[1] += i
        print(*result)
'''

ni = 0
nj = -1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
v = 0
if K > C*R: # K가 가능한 범위를 벗어난 경우 0 출력
    print(0)
else: # 범위 안에 있는 경우
    seat = [[0]*R for _ in range(C)]
    for num in range(1, K+1):
 #델타 탐색 ( 북쪽부터 시작해서 시계방향)
        while True:
            mi = ni + di[v] #임시로 좌표값 부여
            mj = nj + dj[v] # cnt변수를 활용해서 시작 방향을 바꿔줌
            if 0 <= mi < C and 0 <= mj < R and seat[mi][mj] == 0: #인덱스가 범위내이고 값이 0일 경우
                seat[mi][mj] = num # 해당 좌표에 num을 저장
                ni, nj = mi, mj # 시작할 행, 열을 현재 좌표로 설정
                break
            else:
                v = (v+1)%4
    else:
        print(*[ni+1, nj+1]) # 실제 인덱스에서 1씩 더한 값이 좌표값
