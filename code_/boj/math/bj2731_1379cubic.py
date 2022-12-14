T = int(input())
for t in range(T):
    S = list(map(int,list(input()[::-1])))
    l = len(S)
    print(S)
    n = 0
    cub = [0]*3*l
    for i in range(l):
        if cub[:l] == S:
            break
        if i == 0:
            num = S[i] ** 3 % 10
            n += num
            ncub = num ** 3
            cub[1] += ncub//10
            cub[2] += ncub//100
        else:
            for k in range(10):
                c = (3*(10**i)*k*(n**2) + n**3)%(10**(i+1))
                if c//(10**i) == S[i]:
                    n += 10**i*k
                    break
    print(n)