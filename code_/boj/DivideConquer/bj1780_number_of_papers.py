import sys

def paper_check(r, c, n):
    check = True
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != paper[r][c]:
                check = False
                nn = n//3
                for ni in range(3):
                    for nj in range(3):
                        paper_check(r+ni*nn, c+nj*nn, nn)
                break
        if not check:
            break
    else:
        ans[paper[r][c]] += 1

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = [0, 0, 0]
paper_check(0, 0, N)
print(ans[-1], ans[0], ans[1], sep="\n")