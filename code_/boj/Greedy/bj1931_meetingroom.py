# 풀이1
def func(arg):
	global m
	if arg[0] < m[1]:
		return False
	else:
		return True


N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while meeting:
	m = min(meeting, key=lambda x: x[1])
	meeting = list(filter(func, meeting))
	cnt += 1
print(cnt)

# 풀이2
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: x[1] - 1/(1+x[0]))
t = 0
cnt = 0
for m in meeting:
	if m[0] >= t:
		t = m[1]
		cnt += 1
print(cnt)