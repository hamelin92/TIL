T = int(input())
for t in range(T):
	N = int(input())
	rec = [list(map(int, input().split())) for _ in range(N)]
	rec.sort(key=lambda x: x[0]+x[1]+1/(1+x[1]))
	
