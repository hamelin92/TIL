from collections import deque

N = int(input())
check = [False]*(N+1)
ans = 0
que = deque([N])
check[N] = 1
while que:
    q = que.popleft()
    if q == 1:
        break
    q1, q2, q3 = q//3, q//2, q-1
    if not check[q1] and q%3 == 0:
        check[q1] = check[q] + 1
        que.append(q1)
    if not check[q2] and q%2 == 0:
        check[q2] = check[q] + 1
        que.append(q2)
    if not check[q3]:
        check[q3] = check[q] + 1
        que.append(q3)
print(check[q]-1)

