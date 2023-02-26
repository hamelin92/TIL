def multiply(mat1, mat2):
    s1 = mat1[1][0] + mat1[1][1]
    s2 = s1 - mat1[0][0]
    s3 = mat2[0][1]-mat2[0][0]
    s4 = mat2[1][1] - s3
    m2 = mat1[0][0] * mat2[0][0]
    m5 = s1*s3
    t1 = s2*s4+m2
    t2 = t1+(mat1[0][0]-mat1[1][0])*(mat2[1][1]-mat2[0][1])
    return [[(m2+mat1[0][1] * mat2[1][0])%10007, (t1+m5+(mat1[0][1]-s2)*mat2[1][1])%10007],[(t2-mat1[1][1]*(s4-mat2[1][0]))%10007, (t2+m5)%10007]]


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


n = int(input())
f = [[1, 1], [1, 0]]
f_n = matpower(f, n)[0][0]
print(f_n)
