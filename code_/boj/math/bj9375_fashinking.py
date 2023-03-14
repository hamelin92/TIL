from collections import defaultdict

T = int(input())
for t in range(T):
    n = int(input())
    dress = defaultdict(list)
    for i in range(n):
        name, dress_type = input().split()
        dress[dress_type].append(name)
    ans = 1
    for k in dress.keys():
        ans *= len(dress[k])+1
    print(ans-1)