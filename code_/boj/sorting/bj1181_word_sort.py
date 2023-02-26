import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = defaultdict(list)
words = set(sys.stdin.readline().rstrip("\n") for _ in range(N))
for w in words:
    dic[len(w)].append(w)
for key in sorted(dic.keys()):
    dic[key].sort()
    for w in dic[key]:
        print(w)
