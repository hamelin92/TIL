
N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

def multiply(mat1, mat2):
    global N
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum([mat2[k][j] * mat1[i][k] for k in range(N)])%1000
    return result
ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans[i][j] = mat[i][j]%1000
        mat[i][j] %= 1000
seq = []
while B > 1:
    seq.append(B%2)
    B = B//2

for exp in seq[::-1]:
    if exp:
        ans = multiply(multiply(ans, ans), mat)
    else:
        ans = multiply(ans, ans)
for i in range(N):
    print(str(ans[i]).replace("[", "").replace("]", "").replace(",", ""))
