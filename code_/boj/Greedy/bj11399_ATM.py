N = int(input())
P = list(map(int, input().split()))
P.sort(reverse=True)
print(sum(map(lambda x: P[x]*(x+1), range(N))))