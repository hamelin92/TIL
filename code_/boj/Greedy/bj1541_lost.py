expr = input().split("-")
ans = 0
for i in range(len(expr)):
    ex = expr[i]
    if i == 0:
        ans += sum(map(int, ex.split("+")))
    else:
        ans -= sum(map(int, ex.split("+")))
print(ans)