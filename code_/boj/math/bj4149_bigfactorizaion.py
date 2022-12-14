from math import gcd

N = int(input())
x = y = 2
d = 1
while d == 1:
    x = (x ** 2 + 1)%N
    y = (y ** 2 + 1)%N
    y = (y ** 2 + 1)%N
    d = gcd(abs(x-y), N)
if d == N:
    pass
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
i = 0
while True:
    while N % primes[i] == 0:
        N = N // primes[i]
        print(primes[i])
    else:
        if i == len(primes)-1:
            break
        i += 1
rad = int(N**(1/2))+1
j = primes[-1]+2
while j < rad:
    while N%j == 0:
        N = N//j
        print(j)
    else:
        j += 2
