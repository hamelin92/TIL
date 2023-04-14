N, M = map(int, input().split())

def combination(n, picks):
    if len(picks) == M+1:
        print(*picks[1:])
    for i in range(picks[-1]+1, n+1):
        combination(n, picks+[i])

combination(N, [0])