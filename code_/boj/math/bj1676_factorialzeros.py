N = int(input())
c = 5
ans = 0
while N > 4:
    ans += N//5
    N //= 5
print(ans)
