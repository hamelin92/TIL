def solution(grids):
    answer = []
    cases = len(grids)
    for i in range(cases): # 각각의 그림들
        grid = grids[i]
        edges = [None]*4 #왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래 모서리 좌표
        inner_edges = [None]*4
        edge_chker = 0
        R = len(grid)
        C = len(grid[0])
        for j in range(R): # 행 인덱스
            if edge_chker == 4:
                break
            for k in range(C): # 열 인덱스
                if edge_chker == 4:
                    break
                if grid[j][k] == 'X' and edges[0] == None:
                    edges[0] = (j,k)
                    edge_chker += 1
                if grid[j][C-k-1] == 'X' and edges[1] == None:
                    edges[1] = (j, C-k-1)
                    edge_chker += 1
                if grid[R-j-1][k] == 'X' and edges[2] == None:
                    edges[2] = (R-j-1, k)
                    edge_chker += 1
                if grid[R-j-1][C-k-1] == 'X' and edges[3] == None:
                    edges[3] = (R-j-1, C-k-1)
                    edge_chker += 1
        if edges[0][0] != edges[1][0] or edges[0][1] != edges[2][1] or edges[1][1] != edges[3][1] or edges[2][0] != edges[3][0]:
            answer.append(False)
            continue
        else:
            answer.append(True)
            continue
            # edge_chker = 0
            # nj = edges[0][0]
            # nk = edges[0][1]
            # for j in range(edges[2][0] - edges[0][0]+1):
            #     for k in range(edges[1][1] - edges[0][1]+1):
            #         if edge_chker == 4:
            #             break
            #         if grid[nj+j][nk+k] == '.' and inner_edges[0] == None and grid[nj+j-1][nk+k] == grid:
            #             edges[0] = (nj+j, nk+k)
            #             edge_chker += 1
            #         if grid[nj+j][edges[1][1]-k-1] == '.' and inner_edges[1] == None:
            #             edges[1] = (j, C - k - 1)
            #             edge_chker += 1
            #         if grid[edges[2][0] - j - 1][nk+k] == '.' and inner_edges[2] == None:
            #             edges[2] = (R - j - 1, k)
            #             edge_chker += 1
            #         if grid[R - j - 1][C - k - 1] == '.' and inner_edges[3] == None:
            #             edges[3] = (R - j - 1, C - k - 1)
            #             edge_chker += 1
    return answer



'''
문제 설명
당신에게 직사각형 흑백 그림이 여러 개 주어집니다. 당신은 이 흑백 그림이 정확히 하나의 검은색 ㅁ (미음, Consonant 'ㅁ' in the Korean alphabet) 모양을 나타내고 있는지 알고 싶습니다. ㅁ 모양이란 외부는 검은색 직사각형 형태이며, 내부에 흰색 직사각형 구멍이 하나 뚫린 모양을 말합니다. 이때, ㅁ의 각 변의 굵기와 길이는 얼마가 되든 상관없습니다. 즉, ㅁ이 직사각형 모양을 하고 있다던가, 또는 각 변의 굵기가 제각각이더라도 온전한 ㅁ 모양입니다.

그림이 여러 개 담긴 2차원 문자열 배열 grids가 주어졌을 때, 각 그림이 정확히 하나의 검은색 ㅁ 모양을 나타내고 있으면 참값, 아니면 거짓값을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ grids의 행의 개수 ≤ 10
1 ≤ grids의 열의 길이 ≤ 500
1 ≤ grids의 모든 문자열의 길이 ≤ 500
grids의 모든 문자열은 '.'과 'X'로만 이루어져 있습니다.
grids[i][j][k]는 i+1번째 그림의 j+1번째 가로줄의 k+1번째 세로줄의 색상을 의미합니다. 'X'면 해당 위치가 검은색임을, '.'면 해당 위치가 흰색임을 의미합니다.
같은 그림 내의 모든 문자열의 길이는 전부 같습니다.
입출력 예
grids	result
[[".....",".XXX.",".X.X.",".XXX.","....."],["XXXXX","XXXXX","XXX.X","XXX.X","XXXXX"],["XXXXX","X...X","X.X.X","X...X","XXXXX"],["....X",".....","XXX..","X.X..","XXX.."],[".......","XXX.XXX","X.X.X.X","XXX.XXX","......."],["XXXXX","XX.XX","X...X","XX.XX","XXXXX"]]	[true,true,false,false,false,false]
입출력 예 설명
입출력 예 #1

주어진 예시에는 다음과 같은 6개의 그림이 있습니다.
ex1.png

1번째 그림은 온전한 ㅁ 모양을 나타내고 있습니다.
2번째 그림도 온전한 ㅁ 모양을 나타내고 있습니다. 다만 각 변의 굵기가 조금씩 다를 뿐입니다.
3번째 그림은 온전한 ㅁ 모양을 나타내지 않습니다. ㅁ의 내부 공백 안에 검은색으로 칠해진 칸이 있기 때문입니다.
4번째 그림도 온전한 ㅁ 모양을 나타내지 않습니다. ㅁ의 외부에 검은색으로 칠해진 칸이 있기 때문입니다.
5번째 그림은 하나의 온전한 ㅁ 모양을 나타내지 않습니다. ㅁ 모양을 2개 가지고 있기 때문입니다.
6번째 그림은 온전한 ㅁ 모양을 나타내지 않습니다. 내부 공백이 직사각형 형태가 아니기 때문입니다.

'''