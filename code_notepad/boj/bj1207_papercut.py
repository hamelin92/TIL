from pprint import pprint
from copy import deepcopy
def mat_add(arg1, arg2, x = 0, y = 0):
    result = deepcopy(arg1)
    for i in range(len(arg1)):
        for j in range(len(arg1[i])):
            if result[i+x][j+y]*arg2[i][j] > 0:
                return arg1, -1
            else:
                result[i+x][j+y] += arg2[i][j]
    return result, 0


L = int(input())
L_square = [[0]*10 for _ in range(L)]
L_sq_copy = [[0]*10 for _ in range(L)]
U = []
p_size = 0
while p_size < L**2:
    N, M = list(map(int,input().split(' ')))
    S = []
    for idx2 in range(N):
        line = input()
        line = line.replace('#', f'{M}', M)
        line = line.replace('.', '0', M)
        s = ' '.join(line)
        s= list(map(int, s.split()))
        p_size += s.count(1)
        S.append(s)
    U.append(S)
U.sort()
for idx3 in range(L-len(U[0])+1):
    for idx4 in range(L-len(U[0][0]+1)):
        mat_add(L_sq_copy, U[0], idx3, idx4)
        for idx5 in range(len(U)-1):
            for idx6 in range(U)


