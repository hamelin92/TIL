import sys
from collections import defaultdict

def dfs(s, d):
    global far, diameter
    if d > diameter:
        far = s
        diameter = d
    for e, t in tree[s]:
        if not visit[e]:
            visit[e] = True
            dfs(e, d+t)
    

V = int(sys.stdin.readline())
tree = defaultdict(list)
diameter = 0
visit = [False] * (V+1)
for v in range(V):
    s, *connected, dels = map(int, sys.stdin.readline().split())
    n = len(connected)//2
    for e in range(n):
        tree[s].append((connected[2*e], connected[2*e+1]))
        tree[connected[2*e]].append((s, connected[2*e+1]))
far = s
visit[s] = True
dfs(s, 0)
visit = [False] * (V+1)
visit[far] = True
diameter = 0
dfs(far, 0)
print(diameter)