N, K = map(int, input().split())
people = list(range(1, N+1))
yperm = []
idx = 0
while people:
    n = len(people)
    idx = (idx+K-1)%n
    yperm.append(people.pop(idx))
print("<", str(yperm).strip("[").rstrip("]"), ">", sep="")
