N = int(input())
edges = [list(map(int, input().split())) for _ in range(6)]
dir_all = [edges[i][0] for i in range(6)]
directions = [0]*4 
concave = [] # 오목한 구간 방향 찾아서 저장
for i in range(6): # 같은 방향이 2개이상 존재하는 쪽이 오목한 구간
    directions[edges[i][0]-1] += 1
    if directions[edges[i][0]-1] == 2:
        concave.append(edges[i][0])
large = 1
small = 1

for i in range(6):
    # 6개의 변에 대해 순서대로 체크
    # 오목하게 파인 곳의 넓이를 구하는 변들은 concave에 입력한 방향과 양쪽에 인접해있다.
    # 그러므로 양쪽의 방향이 concave에 속할 경우 그때의 변의 길이를 small에 곱해준다.
    if (dir_all[i] in concave) and (dir_all[i+1-6] in concave) and (dir_all[i-1] in concave):
        small *= edges[i][1]
    elif edges[i][0] in concave: #위에서 체크한 경우 외의 concave에 속하는 케이스는 패스해준다.
        continue
    else: # concave에 속한 케이스를 전부 제외하고 나면 크게 둘러싼 직사각형의 변의 길이에 해당한다.
        large *= edges[i][1]
    # 최종적으로 large 넓이에서 small 넓이를 빼고 거기에 참외수를 곱한다.
print(N * (large - small))

