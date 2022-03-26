from pprint import pprint
from collections import deque
n, m = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
wall = []
empty = []
virus = []
dx = [1,-1,0,0]
dy= [0,0,1,-1]
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            wall.append((i,j))
        elif lst[i][j] == 0:
            empty.append((i,j))
        elif lst[i][j] == 2:
            virus.append((i,j))

q = deque(virus)
q.popleft()
visited = []
for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited and lst[nx][ny] == 0:

pprint(lst)
print(wall)
print(empty)
print(virus)