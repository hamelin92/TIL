def gadd(x, y):
    return [x[0]+y[0], x[1]+y[1]]


def gsum(arr):
    return [sum([a[0] for a in arr]), sum([a[1] for a in arr])]


def gmul(x, y):
    global D
    return [x[0]*y[0]+x[1]*y[1]*D, x[0]*y[1]+x[1]*y[0]]


def matadd(mat1, mat2):
    N = len(mat1)
    return [[gadd(mat1[i][j],mat2[i][j]) for j in range(N)] for i in range(N)]


def matadd_c(mat, cons):
    N = len(mat)
    cons_id = [[cons if i == j else [0,0] for j in range(N)] for i in range(N)]
    return [[gadd(mat[i][j], cons_id[i][j]) for j in range(N)] for i in range(N)]


def matmul(mat1, mat2):
    N = len(mat1)
    return [[gsum([gmul(mat1[i][k],mat2[k][j]) for k in range(N)]) for j in range(N)] for i in range(N)]


def matmul_c(mat, cons):
    N = len(mat)
    return [[gmul(mat[i][j], cons) for j in range(N)] for i in range(N)]


def mattr(mat):
    N = len(mat)
    return gsum([mat[i][i] for i in range(N)])


def matpower(mat, B):
    N = len(mat)
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i][j] = mat[i][j]
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2
    for exp in seq[::-1]:
        if exp:
            ans = matmul(matmul(ans, ans), mat)
        else:
            ans = matmul(ans, ans)
    return ans


def charpoly(mat, m):
    N = len(A)
    C = mat[:]
    c = [[1, 0]]
    for k in range(1, N+1):
        if k > 1:
            C = matmul(A, matadd_c(C, c[-1]))
        tr = mattr(C)
        c.append([int(-tr[0]/k), int(-tr[1]/k)])
    return c

def list_chunk(arr, n):
    d = len(arr)//n
    return [arr[k*n:(k+1)*n] for k in range(d)]


n, M, D = map(int, input().split())
A = [list_chunk(list(map(int, input().split())), 2) for _ in range(n)]
poly = charpoly(A, M)
for c_i in poly[::-1]:
    print(f'{c_i[0]%M} {c_i[1]%M}')
