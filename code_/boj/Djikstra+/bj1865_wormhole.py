import sys
from collections import defaultdict

inputs = sys.stdin.readline
sup = 10001

def bellman_ford(start):
    global N, M, W, sup
    weights[start] = 0
    for i in range(N):
        for s in edges.keys():
            for et in edges[s]:
                next_node = et[0]
                nweight = et[1] + weights[s]
                if weights[next_node] > nweight:
                    weights[next_node] = nweight
                    if i == N-1:
                        return True
                
    return False


T = int(inputs())
for testcase in range(T):
    N, M, W = map(int, inputs().split())
    weights = [sup]*(1+N)
    edges = defaultdict(list)
    for m in range(M):
        s, e, t = map(int, inputs().split())
        edges[s].append((e, t))
        edges[e].append((s, t))
    for w in range(W):
        s, e, t = map(int, inputs().split())
        edges[s].append((e, -t))
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
