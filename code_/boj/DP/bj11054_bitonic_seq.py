N = int(input())
A = list(map(int, input().split()))
dp_inc = [1]*(N+1)
dp_dec = [1]*(N+1)
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
        if A[N-i-1] > A[N-j-1]:
            dp_dec[N-i-1] = max(dp_dec[N-i-1], dp_dec[N-j-1] + 1)
print(max(dp_inc[k]+dp_dec[k] for k in range(N))-1)
