L = int(input())
data = input()
coef = {chr(i): i-96 for i in range(97, 123)}
weights = 1
ans = 0
for i in range(L):
    ans = (ans + coef[data[i]]*weights)%1234567891
    weights *= 31
print(ans)
