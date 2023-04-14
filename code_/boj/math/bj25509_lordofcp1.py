# import sys

# def multiply(mat1, mat2):
#     # mat1, mat2 : 2 by 2 matrices
#     s1 = mat1[1][0] + mat1[1][1]
#     s2 = s1 - mat1[0][0]
#     s3 = mat2[0][1]-mat2[0][0]
#     s4 = mat2[1][1] - s3
#     m2 = mat1[0][0] * mat2[0][0]
#     m5 = s1*s3
#     t1 = s2*s4+m2
#     t2 = t1+(mat1[0][0]-mat1[1][0])*(mat2[1][1]-mat2[0][1])
#     return [[m2+mat1[0][1] * mat2[1][0], t1+m5+(mat1[0][1]-s2)*mat2[1][1]],[t2-mat1[1][1]*(s4-mat2[1][0]), t2+m5]]

# def matadd(A, B):
#     N = len(A)
#     result = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             result[i][j] = A[i][j] + B[i][j]
#     return result

# def matadd_c(A, const):
#     N = len(A)
#     result = [r[:] for r in A[:]]
#     for i in range(N):
#         result[i][i] += const
#     return result

# def matsub(A, B):
#     N = len(A)
#     result = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             result[i][j] = A[i][j] - B[i][j]
#     return result

# def strassen_mul(A, B):
#     # A, B must be 2**k by 2**k matrices
#     N = len(A)
#     if N == 2:
#         return multiply(A, B)
#     n = N//2
#     A11 = [c[:n] for c in A[:n]]
#     A12 = [c[n:] for c in A[:n]]
#     A21 = [c[:n] for c in A[n:]]
#     A22 = [c[n:] for c in A[n:]]
#     B11 = [c[:n] for c in B[:n]]
#     B12 = [c[n:] for c in B[:n]]
#     B21 = [c[:n] for c in B[n:]]
#     B22 = [c[n:] for c in B[n:]]
#     S1 = matadd(A21, A22)
#     S2 = matsub(S1, A11)
#     S3 = matsub(B12, B11)
#     S4 = matsub(B22, S3)
#     M1 = strassen_mul(S2, S4)
#     M2 = strassen_mul(A11, B11)
#     M3 = strassen_mul(A12, B21)
#     M4 = strassen_mul(matsub(A11, A21), matsub(B22, B12))
#     M5 = strassen_mul(S1, S3)
#     M6 = strassen_mul(matsub(A12, S2), B22)
#     M7 = strassen_mul(A22, matsub(S4, B21))
#     T1 = matadd(M1, M2)
#     T2 = matadd(T1, M4)
#     C11 = matadd(M2, M3)
#     C12 = matadd(T1, matadd(M5, M6))
#     C21 = matsub(T2, M7)
#     C22 = matadd(T2, M5)
#     return [C11[i]+C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]

# def strassen(A, B):
#     N = len(A)
#     resize = 1<<(N-1).bit_length()
#     dif = resize-N
#     if N != resize:
#         A_ex = [A[i][:]+[0]*dif if i < N else [0]*resize for i in range(resize)]
#         B_ex = [B[i][:]+[0]*dif if i < N else [0]*resize for i in range(resize)]
#     else:
#         A_ex = A
#         B_ex = B
#     res = strassen_mul(A_ex, B_ex)
#     return [res[i][:N] for i in range(N)]

# def mattr(mat):
#     N = len(mat)
#     return sum([mat[i][i] for i in range(N)])


# def charpoly(mat):
#     N = len(A)
#     c = [1] + [False]*N
#     for k in range(1, N+1):
#         if k > 1:
#             mat = strassen(A, matadd_c(mat, c[k-1]))
#         tr = mattr(mat)
#         c[k] = -tr//k
#     return c

# n, M = map(int, sys.stdin.readline().split())
# A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# I = [[0]*n for _ in range(n)]
# for i in range(n):
#     I[i][i] = 1
# poly = charpoly(A)
# for c_i in poly[::-1]:
#     print(c_i%M)
import sys
from math import gcd
from itertools import permutations


def det(M):
    # 입력 행렬 M의 행과 열의 개수를 구합니다
    n = len(M)

    # 행렬식을 계산하기 위한 변수 det_value를 1로 초기화합니다
    det_value = 1
    
    # 가우스 소거법을 사용하여 행렬을 상삼각행렬로 변환합니다
    for i in range(n):
        # 대각 원소가 0인 경우 행 교환을 수행합니다
        if M[i][i] == 0:
            for j in range(i+1, n):
                if M[j][i] != 0:
                    M[i], M[j] = M[j], M[i]
                    det_value *= -1
                    break
        
        # 대각 원소가 0이 아닌 경우 대각선 방향으로 가우스 소거법을 수행합니다
        if M[i][i] != 0:
            for j in range(i+1, n):
                c = M[j][i] / M[i][i]
                for k in range(i, n):
                    M[j][k] -= c * M[i][k]
                    
    # 대각선 원소를 곱하여 행렬식을 계산합니다
    for i in range(n):
        det_value *= M[i][i]
    
    return det_value


def hermite_interpolation(A):
    n = len(A)
    I = [[int(i==j) for j in range(n)] for i in range(n)]
    
    lambda_list = [A[i][i] for i in range(n)]
    
    def h(x, i):
        # H(x) 계산 함수
        B = [[A[j][k] - x * I[j][k] for k in range(n)] for j in range(n) if j != i]
        return det(B) / det([[B[j][k] for k in range(n-1)] for j in range(n-1)])
    
    poly = [1]
    for i in range(n):
        poly = [0] + poly
        term = [h(lambda_list[i], j) for j in range(i+1)]
        for j in range(i+1):
            term[j] *= (-1)**(i-j) * poly[j]
            if j < i:
                term[j] += (-1)**(i-j-1) * poly[j+1]
        poly = term
        
    return poly

def bairstow(A):
    n = len(A)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    b[n] = 1
    c[n - 1] = 1
    for i in range(n - 1, -1, -1):
        d = A[i] - b[i + 2] * c[i + 2] - b[i + 1] * c[i + 1]
        if c[i + 1] == 0:
            b[i] = 0
        else:
            b[i] = (c[i + 1] * d - A[i + 1]) / (c[i + 1] ** 2 - b[i + 1] * c[i + 2])
        if b[i + 1] == 0:
            c[i] = 0
        else:
            c[i] = (b[i + 1] * d - A[i]) / (b[i + 1] ** 2 - b[i + 2] * c[i + 1])
    return c[2:], c[1:-1]

def characteristic_poly(A):
    n = len(A)
    if n == 1:
        return [1, -A[0][0]]
    elif n == 2:
        return [1, -A[0][0]-A[1][1], A[0][0]*A[1][1]-A[0][1]*A[1][0]]
    else:
        B = [-1] * (n + 1)
        C = [-1] * (n + 1)
        B[0], B[1] = 1, -A[0][0]
        C[0], C[1] = 1, -A[0][0]
        for i in range(n - 1, 1, -1):
            C[i - 1:i + 1], B[i] = bairstow([A[j][i] for j in range(i, n)] + [A[j][i - 1] for j in range(i - 1, n - 1)] + [C[i], C[i - 1]])
        C[1], B[2] = bairstow([A[1][1], A[1][0], C[2], C[1]])
        return [1] + [-x for x in B[1:]] + [-C[0]]

n, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
poly_c = characteristic_poly(mat)
print(poly_c)
