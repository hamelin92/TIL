import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
colors = [0, 0]

def cut_paper(r, c, n):
    if n == 1:
        colors[paper[r][c]] += 1
        return
    subdim = n//2
    det = sum(paper[r][c:c+n])
    for i in range(r, r+n):
        if det%n != 0 or sum(paper[i][c:c+n]) != det:
            cut_paper(r, c, subdim)
            cut_paper(r+subdim, c, subdim)
            cut_paper(r, c+subdim, subdim)
            cut_paper(r+subdim, c+subdim, subdim)
            return
    if det > 0:
        colors[1] += 1
        return
    colors[0] += 1
    return

cut_paper(0, 0, N)
print(*colors, sep="\n")
