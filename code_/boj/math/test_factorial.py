import time

def matmul_ijk(mat1, mat2):
    N = len(mat2)
    return [[sum(row[k]*mat2[k][j] for k in range(N)) for j in range(N)] for row in mat1]

def multiply(mat1, mat2):
    # mat1, mat2 : 2 by 2 matrices
    s1 = mat1[1][0] + mat1[1][1]
    s2 = s1 - mat1[0][0]
    s3 = mat2[0][1]-mat2[0][0]
    s4 = mat2[1][1] - s3
    m2 = mat1[0][0] * mat2[0][0]
    m5 = s1*s3
    t1 = s2*s4+m2
    t2 = t1+(mat1[0][0]-mat1[1][0])*(mat2[1][1]-mat2[0][1])
    return [[m2+mat1[0][1] * mat2[1][0], t1+m5+(mat1[0][1]-s2)*mat2[1][1]],[t2-mat1[1][1]*(s4-mat2[1][0]), t2+m5]]


def matadd(A, B):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = A[i][j] + B[i][j]
    return result


def matsub(A, B):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = A[i][j] - B[i][j]
    return result


def strassen_mul(A, B):
    # A, B must be 2**k by 2**k matrices
    N = len(A)
    if N == 2:
        return multiply(A, B)
    n = N//2
    A11 = [c[:n] for c in A[:n]]
    A12 = [c[n:] for c in A[:n]]
    A21 = [c[:n] for c in A[n:]]
    A22 = [c[n:] for c in A[n:]]
    B11 = [c[:n] for c in B[:n]]
    B12 = [c[n:] for c in B[:n]]
    B21 = [c[:n] for c in B[n:]]
    B22 = [c[n:] for c in B[n:]]
    S1 = matadd(A21, A22)
    S2 = matsub(S1, A11)
    S3 = matsub(B12, B11)
    S4 = matsub(B22, S3)
    M1 = strassen_mul(S2, S4)
    M2 = strassen_mul(A11, B11)
    M3 = strassen_mul(A12, B21)
    M4 = strassen_mul(matsub(A11, A21), matsub(B22, B12))
    M5 = strassen_mul(S1, S3)
    M6 = strassen_mul(matsub(A12, S2), B22)
    M7 = strassen_mul(A22, matsub(S4, B21))
    T1 = matadd(M1, M2)
    T2 = matadd(T1, M4)
    C11 = matadd(M2, M3)
    C12 = matadd(T1, matadd(M5, M6))
    C21 = matsub(T2, M7)
    C22 = matadd(T2, M5)
    return [C11[i]+C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]


def strassen(A, B):
    N = len(A)
    resize = 1<<(N-1).bit_length()
    dif = resize-N
    if N != resize:
        A_ex = [A[i][:]+[0]*dif if i < N else [0]*resize for i in range(resize)]
        B_ex = [B[i][:]+[0]*dif if i < N else [0]*resize for i in range(resize)]
    else:
        A_ex = A
        B_ex = B
    res = strassen_mul(A_ex, B_ex)
    return [res[i][:N] for i in range(N)]


N = int(input())
A = [list(range(i, N+i)) for i in range(N)]
print("start")
start_str = time.time()
strassen(A, A)
print("strassen",time.time()-start_str)
start_ijk = time.time()
matmul_ijk(A, A)
print("ijk",time.time()-start_str)