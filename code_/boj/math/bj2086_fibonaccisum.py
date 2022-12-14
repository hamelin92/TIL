def multiply(mat1, mat2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result[i][j] = sum([mat2[k][j] * mat1[i][k] for k in range(2)])%1000000000
    return result


def matpower(mat, B):
    ans = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            ans[i][j] = mat[i][j]
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2
    for exp in seq[::-1]:
        if exp:
            ans = multiply(multiply(ans, ans), mat)
        else:
            ans = multiply(ans, ans)
    return ans


a, b = map(int, input().split())
f = [[1, 1], [1, 0]]
f_a = matpower(f, a)[0][0]
f_b = matpower(f, b+1)[0][0]
if f_b < f_a:
    f_b += 1000000000
print((f_b-f_a))