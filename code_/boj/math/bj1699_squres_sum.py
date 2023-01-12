N = int(input())
def sum_of_squares(n):
    while n%4 == 0 and n > 0:
        n = n // 4
    if n%8 == 7:
        return 4
    if n - int(n**0.5)**2 == 0:
        return 1
    for j in range(2, int(n ** (1/2))+1):
        if n%j == 0:
            factor = 0
            while n%j == 0:
                n = n//j
                factor += 1
            if j%4 == 3 and factor%2 == 1:
                return 3
    else:
        if n%4 == 3:
            return 3
    return 2
print(sum_of_squares(N))