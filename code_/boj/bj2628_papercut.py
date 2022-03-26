

n, m = map(int, input().split())
cut = int(input())
# 가로길이, 세로길이, 자르는 횟수 입력 받기
rows = [0, m]
cols = [0, n]
#가로,세로로 자르는 번호를 담을 리스트, 양쪽 끝을 초기값으로 보유
cuts = [list(map(int, input().split())) for _ in range(cut)]
#자르는 번호 입력 받기
for mv in cuts:
    if mv[0] == 0:
        rows.append(mv[1])
    else:
        cols.append(mv[1])
#가로로 자르는 것과 세로로 자르는 것을 분류하여 번호값만 따로 리스트에 저장
rows.sort()
cols.sort()
#각각 정렬
areas = []
#넓이를 담을 리스트
for row_num in range(len(rows)-1):
    for col_num in range(len(cols)-1):
        r1 = rows[row_num+1] - rows[row_num]
        r2 = cols[col_num+1] - cols[col_num]
        areas.append(r1 * r2)
#행과 열 리스트에 대해 모든 경우를 조합하여 그 사이의 넓이를 계산하고 리스트에 저장
print(max(areas))
#넓이 리스트에서 최대값을 출력



#10 8
#8
#0 3
#1 4
#0 1
#0 5
#0 4
#1 2
#1 1
#1 3