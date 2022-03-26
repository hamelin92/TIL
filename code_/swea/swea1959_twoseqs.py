T = int(input()) # 테스트 케이스 수
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 각 숫자열의 길이 ( 3 ~ 20 )
    A = list(map(int, input().split())) # 길이가 N인 숫자열
    B = list(map(int, input().split())) # 길이가 M인 숫자열

    values = [] # max값을 그떄그때 계산해서 갱신해주는 방법도 있겠지만 값이 음수일수도 있기 떄문에..

    if N >= M:# A의 숫자열이 더 길거나 같은 경우
        for i in range(N-M+1): # A의 시작지점을 지정
            tmp = 0
            for j in range(M): # B에 대해 순회
                tmp += A[i+j] * B[j] # B의 index에 대해 A는 위에서 정한 시작지점부터 계산.
            values.append(tmp) # 값이 계산되면 이를 리스트에 넣어준다.
    else: # 반대의 경우 (나머지는 위와 동일, index값만 반대로 바꿔주기)
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += A[j] * B[i + j]
            values.append(tmp)
    print(f'#{tc} {max(values)}') # values 리스트에서 최대값을 구해서 출력한다.