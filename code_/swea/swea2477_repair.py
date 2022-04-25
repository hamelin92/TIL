from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M,K,A,B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(enumerate(map(int, input().split()), 1))
    answer = 0
    time_k = t[0][1]
    a_now = [0] * N
    a_rec = [0] * N
    b_now = [0] * M
    a_que = deque(t)
    a_que.append((2000, 22001))
    b_que = deque([])
    now = 0
    a_cnt = 0
    while a_que:
        q = a_que.popleft()
        for i in range(N):
            if a_now[i] <= q[1]:
                match = i
                break
        else:
            match = 0
            for j in range(1,N):
                if a_now[match] > a_now[j]:
                    match = j
        time_now = max(a_now[match], q[1])
        send = []
        for i in range(N):
            if a_now[i] <= time_now and a_rec[i] > 0:
                send.append((i, a_now[i], a_rec[i]))
                a_rec[i] = 0
        send.sort(key=lambda x: N*x[1] + x[0])
        for s in send:
            b_que.append(s)
        a_now[match] = time_now + a[match]
        a_rec[match] = q[0]

    while b_que:
        q = b_que.popleft()
        for i in range(M):
            if b_now[i] <= q[1]:
                match = i
                break
        else:
            match = 0
            for j in range(1,M):
                if b_now[match] > b_now[j]:
                    match = j
        b_now[match] = max(b_now[match], q[1]) + b[match]
        if q[0] == A-1 and match == B-1:
            answer += q[2]
    if answer == 0:
        answer = -1
    print(f'#{tc} {answer}')
