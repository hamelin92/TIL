N, M = map(int, input().split())
board = [input() for _ in range(N)]
colors = ["B", "W"]
min_cnt = N*M
for n in range(N-7):
    for m in range(M-7):
        even_cnt = 0
        odd_cnt = 0
        for i in range(8):
            for j in range(8):
                if colors[(i+j)%2] != board[n+i][m+j]:
                    even_cnt += 1
                if colors[(i+j+1)%2] != board[n+i][m+j]:
                    odd_cnt += 1
        tmp_min = min(even_cnt, odd_cnt)
        if tmp_min < min_cnt:
            min_cnt = tmp_min
print(min_cnt)
