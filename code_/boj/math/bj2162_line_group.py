import sys
sys.getrecursionlimit=100000

def is_ccw(origin, start, end):
    det = (start[0] - origin[0])*(end[1]-origin[1]) - (start[1]-origin[1])*(end[0]-origin[0])
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0


def is_crossing(arr1: list, arr2: list):
    u1, u2 = arr1[:2], arr1[2:]
    v1, v2 = arr2[:2], arr2[2:]
    check1 = is_ccw(u1, u2, v1)*is_ccw(u1, u2, v2)
    check2 = is_ccw(v1, v2, u1)*is_ccw(v1, v2, u2)
    if check1 == 0 and check2 == 0:
        if u1 > u2:
            u1, u2 = u2, u1
        if v1 > v2:
            v1, v2 = v2, v1
        if u1 <= v2 and v1 <= u2:
            return True
        else:
            return False
    if check1 <= 0 and check2 <= 0:
        return True
    return False


def find(n):
    if groups[n] != n:
        groups[n] = find(groups[n])
    return groups[n]

def union(n1, n2):
    g1 = find(n1)
    g2 = find(n2)
    if g1 >= g2:
        groups[g1] = g2
    else:
        groups[g2] = g1

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
groups = list(range(N))
g_cnt = [0]*3001
for i in range(N-1):
    for j in range(i+1, N):
        if find(i) != find(j):
            if is_crossing(lines[i], lines[j]):
                union(i, j)
for i in range(N):
    find(i)
for g in groups:
    g_cnt[g] += 1
print(len(set(groups)))
print(max(g_cnt))