N = int(input())
M = int(input())
S = input()
str_dic = {"I": 1, "O": 0}
P = [0] * (M//2+1)
ans = 0
cnt = 0
for i in range(M):
    if not cnt and S[i] == "I":
        cnt = 1
    elif cnt and S[i] != S[i-1]:
        cnt += 1
    elif cnt and S[i] == S[i-1]:
        P[(cnt-1)//2] += 1
        cnt = str_dic[S[i]]
else:
    if cnt >= 3:
        P[(cnt-1)//2] += 1
for m in range(N, len(P)):
    ans += P[m]*(m-N+1)
print(ans)