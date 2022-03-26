N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
cnt = [[0]*7 for _ in range(2)] # 학생 수를 체크할 리스트
rooms = [[0]*7 for _ in range(2)] # 방 수를 체크할 리스트
for student in students: # 각각의 학생에 대해 순회
    cnt[student[0]][student[1]] += 1 # 해당 성별 학년의 카운트 +1
    if rooms[student[0]][student[1]] == 0: # 만약 방이 없는 경우 1로 방을 생성
        rooms[student[0]][student[1]] = 1
    elif cnt[student[0]][student[1]] > K: # 같은 성별 학년에 K를 넘어서면 K만큼의 인원을 따로 방 배정
        cnt[student[0]][student[1]] -= K # 즉 학생수 카운트 -K 동시에 방 수 카운트 +1
        rooms[student[0]][student[1]] +=1

print(sum(rooms[0]) + sum(rooms[1])) #남자방의 카운트 합 + 여자방의 카운트 합 출력