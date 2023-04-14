N = int(input())
arr = list(map(int, input().split()))
ans = [arr[0], arr[-1]]
s = 0
e = N-1
min_val = 2000000001
while s < e:
    val = arr[e] + arr[s]
    if abs(val) < min_val:
        ans[0] = arr[s]
        ans[1] = arr[e]
        min_val = abs(val)
    if val == 0:
        ans[0] = arr[s]
        ans[1] = arr[e]
        min_val = 0
        break
    elif val > 0:
        e -= 1
    else:
        s += 1
print(*ans)
