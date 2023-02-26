S = input()
res = {chr(i): -1 for i in range(97, 123)}
for s in range(len(S)):
    if res[S[s]] == -1:
        res[S[s]] = s
print(*res.values())