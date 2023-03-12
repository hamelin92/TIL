import sys
from collections import defaultdict

N = int(sys.stdin.readline())
members = defaultdict(list)
for i in range(N):
    year, name = sys.stdin.readline().strip("\n").split()
    members[int(year)].append(name)
for k in sorted(members.keys()):
    for m in members[k]:
        print(k, m)
        