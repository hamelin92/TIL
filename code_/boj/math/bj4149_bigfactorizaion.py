from math import gcd, sqrt, floor
from random import sample, randint
from itertools import count


def primes(M: int):
    sieve = [1]*(M+1)
    prime_list = []
    for p in range(2, M+1):
        if sieve[p]:
            prime_list.append(p)
            sieve[p::p] = [0] * (M//p)
    return prime_list


def euclid_algo(m, b):
    # m*p + b*q = gcd(m,b) mod m -> return [gcd(m,b), q]
    # m : modulo
    r = [m, b]
    s = [1, 0]
    t = [0, 1]
    while r[0]%r[1]:
        q = r[0]//r[1]
        r[0], r[1] = r[1], r[0] - q * r[1]
        s[0], s[1] = s[1], s[0] - q * s[1]
        t[0], t[1] = t[1], t[0] - q * t[1]
    return [r[1], t[1]]


def elliptic_curve(x, y, a, m):
    # y**2 = x**3 + ax + b mod m
    # [a, b, m]
    return [a, (y**2 - x ** 3 - a * x)%m, m]


def elliptic_sum(P, Q, E):
    # P, Q : diff pts of a elliptic curve([x,y]), E: elliptic curve, m: modulo
    m = E[2]
    dx = (P[0] - Q[0])%m
    dy = (P[1] - Q[1])%m
    if P[1] == 0:
        return Q
    if Q[1] == 0:
        return P
    if dx or dy:
        if dy%dx:
            inv = euclid_algo(m, dx)
            # if k=mod_inv[0] > 1, k|m
            if inv[0] > 1:
                return inv[0]
            s = dy*inv[1]%m
        else:
            s = dy//dx
        nx = s**2 - P[0] - Q[0]
    else:
        if (3 * P[0] ** 2 + E[0]) % (2 * P[1]):
            inv = euclid_algo(m, 2 * P[1])
            if inv[0] > 1:
                    return inv[0]
            s = (3 * P[0] ** 2 + E[0]) * inv[1] % m
        else:
            s = (3 * P[0] ** 2 + E[0]) % (2 * P[1])
        nx = s ** 2 - 2*P[0]
    ny = P[1] + s * (nx-P[0])
    return [nx, ny]


def n_elliptic_sum(n, P, E):
    Q = P[:]
    seq = []
    while n > 1:
        seq.append(n%2)
        n = n//2
    for add in seq[::-1]:
        if add:
            Q = elliptic_sum(Q, Q, E)
            if type(Q) == int:
                return Q
            Q = elliptic_sum(Q, P, E)
            if type(Q) == int:
                return Q
        else:
            Q = elliptic_sum(Q, Q, E)
            if type(Q) == int:
                return Q
    return Q


def lenstra(n: int, prime_list: list):
    p = [randint(1, n-1), randint(1, n-1)]
    E = elliptic_curve(p[0], p[1], randint(1, n-1), n)
    for pn in prime_list:
        p = n_elliptic_sum(pn, p, E)
        if type(p) == int:
            return p
    return 1


def pollards(number):
    x = 2
    for cycle in count(1):
        y = x
        for i in range(2 ** cycle):
            x = (x * x + 1) % number
            factor = gcd((x - y), number)
            if factor > 1:
                return factor
    return 1


n = int(input())
p_list = primes(n.bit_length())
divs = []
factors = []
while n > 1:
    divisor = lenstra(n, p_list)
    if divisor == 1:
        divs.append(n)
        break
    divs.append(divisor)
    n //= divisor
for d in divs:
    while d > 1:
        factor = pollards(d)
        if factor > 1:
            factors.append(factor)
            d //= factor
    if d > 1:
        factors.append(d)
factors.sort()
for f in factors:
    print(f)
