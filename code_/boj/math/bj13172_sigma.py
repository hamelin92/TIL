import sys
from math import gcd
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


def expectation(n, s):
    d = gcd(n, s)
    nn = n//d
    ss = s//d
    if nn == 1:
        return ss
    else:
        return ss*euclid_algo(1000000007, nn)[1]%1000000007

M = int(sys.stdin.readline())
dices = [expectation(*map(int, sys.stdin.readline().split())) for _ in range(M)]
print(sum(dices)%1000000007)
