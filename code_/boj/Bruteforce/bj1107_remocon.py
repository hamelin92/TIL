from collections import deque

N = input()
num = int(N)
length = len(N)
M = int(input())
buttons = set(range(10))
if M:
    buttons -= set(map(int, input().split()))
min_cnt = abs(num - 100)
start = buttons-{0}
for s in buttons:
    if abs(s-num)+1 < min_cnt:
        min_cnt = abs(s-num)+1
que = deque(start)
if que:
    for l in range(2, length+2):
        ql = len(que)
        for i in range(ql):
            q = que.popleft()
            for b in buttons:
                nq = 10*q + b
                if abs(num-nq)+l < min_cnt:
                    min_cnt = abs(num-nq)+l
                que.append(nq)
print(min_cnt)
