import math

N = int(input())
def sum_of_squares(n):
    while n and n%4 == 0:
        n = n // 4
    if n%8 == 7:
        return 4
    if n - int(math.sqrt(n))**2 == 0:
        return 1
    for j in range(2, int(n ** (1/2))+1):
        if n%j == 0:
            factor = False
            while n and n%j == 0:
                n = n//j
                factor = not factor
            if j%4 == 3 and factor:
                return 3
    else:
        if n%4 == 3:
            return 3
    return 2
print(sum_of_squares(N))