def gadd(x, y):
    return [x[0]+y[0], x[1]+y[1]]


def gsum(arr):
    return [sum([a[0] for a in arr]), sum([a[1] for a in arr])]


def gmul(x, y):
    global D
    return [x[0]*y[0]+x[1]*y[1]*D, x[0]*y[1]+x[1]*y[0]]


def matadd(mat1, mat2):
    N = len(mat1)
    return [[mat1[i][j]+mat2[i][j] for j in range(N)] for i in range(N)]


def matadd_c(mat, cons):
    N = len(mat)
    return [[mat[i][j]+cons if i == j else mat[i][j] for j in range(N)] for i in range(N)]


def matmul(mat1, mat2):
    N = len(mat1)
    return [[sum([mat1[i][k]*mat2[k][j] for k in range(N)]) for j in range(N)] for i in range(N)]


def matmul_c(mat, cons):
    N = len(mat)
    return [[mat[i][j]*cons for j in range(N)] for i in range(N)]


def mattr(mat):
    N = len(mat)
    return sum([mat[i][i] for i in range(N)])


def charpoly(mat, m):
    N = len(A)
    c = [1]
    for k in range(1, N+1):
        if k > 1:
            mat = matmul(A, matadd_c(mat, c[-1]))
        tr = mattr(mat)
        c.append(-tr//k)
    return c


n, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
poly = charpoly(A, M)
for c_i in poly[::-1]:
    print(c_i%M)
