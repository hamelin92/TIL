from itertools import permutations
from pprint import pprint
from copy import deepcopy

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            if cells[i][j] == 1:
                cores.append((i,j))
    M = len(cores)
    permute_iter = list(range(M))
    min_val = 200
    max_core = 0
    for n in range(M):
        check = deepcopy(cells)
        tmp_min = 0
        tmp_core = 0
        for j in range(n,M+n):
            i = j%M
            direc = [1,1,1,1]
            si, sj = cores[i][0], cores[i][1]
            for d in range(4):
                k = 1
                while 0 <= si + k*di[d] < N and 0 <= sj+k*dj[d] < N:
                    ni = si + k*di[d]
                    nj = sj + k*dj[d]
                    if 0 <= ni < N and 0 <= nj < N and check[ni][nj] == 0:
                        k += 1
                        direc[d] += 1
                    else:
                        direc[d] = -1
                        break
            for d in range(4):
                ways = []
                if direc[d] > 0:
                    ways.append([d,direc[d]])
            ways.sort(key=lambda x: x[1])
            print(ways)
            if len(ways) == 0:
                continue
            else:
                nd = ways[0][0]
                length = ways[0][1]
                tmp_core += 1
                tmp_min += length-1
                for w in range(1, length):
                    ni = si+w*di[nd]
                    nj = sj+w*dj[nd]
                    check[ni][nj] = 1

        else:

            if tmp_core > max_core:
                max_core = tmp_core
                min_val = tmp_min
            elif tmp_core == max_core:
                if min_val > tmp_min:
                    min_val = tmp_min
    print(f'#{tc} {min_val}')



