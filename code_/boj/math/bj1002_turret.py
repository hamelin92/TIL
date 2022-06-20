T = int(input())
for tc in range(T):
	x1,y1,r1,x2,y2,r2 = map(int, input().split())
	if x1 == x2 and y1 == y2 and r1 == r2:
		print(-1)
	else:
		d = (x1-x2)**2 + (y1-y2)**2
		long = (r1+r2)**2
		short = abs(r1-r2)**2
		if d > long or d < short:
			print(0)
		elif d == long or d == short:
			print(1)
		else:
			print(2)