lamps = list(input())
N = len(lamps)
def toggle(a): # Y를 N으로, N을 Y로 바꿔주는 토글 함수
    if a == 'Y':
        return 'N'
    else:
        return 'Y'
cnt = 0 # 스위치 누르는 횟수 카운트
for i in range(N):
    if lamps[i] == 'Y': # 켜져있는 램프 발견시 스위치를 누른다.
        cnt += 1 # 스위치 카운트 +1
        for j in range(i,N,i+1): #스위치 번호의 배수인 램프를 모두 토글한다.
            lamps[j] = toggle(lamps[j])
print(cnt)