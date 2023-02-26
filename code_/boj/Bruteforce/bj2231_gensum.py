N = input()
length = len(N)
n = int(N)
for i in range(max(1, n-9*length), n+1):
    res = tmp = i
    while tmp:
        res += tmp%10
        tmp //= 10
    if res == n:
        print(i)
        break
else:
    print(0)