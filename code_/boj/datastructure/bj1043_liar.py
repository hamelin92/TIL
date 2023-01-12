N, M = map(int, input().split())
det = sum(map(lambda x: 1 << (int(x)-1), input().split()[1:]))
parties = [list(map(int, input().split())) for _ in range(M)]
members = [0 for _ in range(M)]
for party in range(M):
    for person in parties[party][1:]:
        members[party] |= 1 << (person-1)
check = set(members)
while check:
    for m in check:
        if det&m > 0:
            det |= m
            check.remove(m)
            break
    else:
        break
print(len(list(filter(lambda x: x&det == 0, members))))
