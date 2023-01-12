from random import randint
from math import gcd, sqrt, floor
from itertools import count
import time
# Sieve of Eratosthenes
def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in range(p, n + 1, p):
                b[i] = False
    return ps


# Finds modular inverse
# Returns inverse, unused helper and gcd
def modular_inv(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = modular_inv(b, r)
    return y, x - q * y, g


# Addition in Elliptic curve modulo m space
def elliptic_add(p, q, a, b, m):
    # If one point is infinity, return other one
    if p[2] == 0: return q
    if q[2] == 0: return p
    if p[0] == q[0]:
        if (p[1] + q[1]) % m == 0:
            return 0, 1, 0  # Infinity
        num = (3 * p[0] * p[0] + a) % m
        denom = (2 * p[1]) % m
    else:
        num = (q[1] - p[1]) % m
        denom = (q[0] - p[0]) % m
    inv, _, g = modular_inv(denom, m)
    # Unable to find inverse, arithmetic breaks
    if g > 1:
        return 0, 0, denom  # Failure
    z = (num * inv * num * inv - p[0] - q[0]) % m
    return z, (num * inv * (p[0] - z) - p[1]) % m, 1


# Multiplication (repeated addition and doubling)
def elliptic_mul(k, p, a, b, m):
    r = (0, 1, 0)  # Infinity
    while k > 0:
        # p is failure, return it
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = elliptic_add(p, r, a, b, m)
        k = k // 2
        p = elliptic_add(p, p, a, b, m)
    return r


# Lenstra's algorithm for factoring
# Limit specifies the amount of work permitted
def lenstra(n, limit):
    g = n
    while g == n:
        # Randomized x and y
        q = randint(0, n - 1), randint(0, n - 1), 1
        # Randomized curve coefficient a, computed b
        a = randint(0, n - 1)
        b = (q[1] * q[1] - q[0] * q[0] * q[0] - a * q[0]) % n
        g = gcd(4 * a * a * a + 27 * b * b, n)  # singularity check
    # If we got lucky, return lucky factor
    if g > 1:
        return g
    # increase k step by step until lcm(1, ..., limit)
    for p in primes(limit):
        pp = p
        while pp < limit:
            q = elliptic_mul(p, q, a, b, n)
            # Elliptic arithmetic breaks
            if q[2] > 1:
                return gcd(q[2], n)
            pp = p * pp
    return False


def pollards(number):
    x = 2
    for cycle in count(1):
        y = x
        for i in range(2 ** cycle):
            x = (x * x + 1) % number
            factor = gcd((x - y), number)
            if factor > 1:
                return factor
    return False

def fast_power(a, p, m):
    # return a ** p mod m
    b = a
    pows = []
    while p:
        pows.append(p%2)
        p >>= 1
    for q in pows[::-1]:
        if q:
            b = (b ** 2) * a
        else:
            b = (b ** 2)
        b = b%m
    return b
    

def miller_rabin(m, k):
    # m > 18
    alpha = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 73]
    s = 0
    d = m-1
    while d%2 == 0:
        d >>= 1
        s += 1
    for a in alpha[:k]:
        for r in range(s):
            if fast_power(a, d, m) != 1:
                if fast_power(a, d*(2**r), m) != m-1:
                    return False
    return True


def factorization(n):
    factors = []
    prime_list = primes(floor(sqrt(n)) + 1)
    for p in prime_list:
        while n%p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


def factor_list(n: int):
    factors = []
    while n%2 == 0:
        n >>= 1
        factors.append(2)
    if n > 100 and miller_rabin(n, 7):
        factors.append(n)
    while n > 1:
        factor = pollards(n)
        if factor > 1:
            n //= factor
            factors.append(factor)
        else:
            break
    if n > 1:
        factors.append(n)
    factors.sort()
    return factors

for i in range(2, 10000):
    start1 = time.time()
    fl1 = factorization(i)
    end1 = time.time() - start1
    start2 = time.time()
    fl2 = factor_list(i)
    end2 = time.time() - start2
    print(end1, end2)
    if fl1 != fl2:
        print(fl1)
        print('###########')
        print(fl2)
        break