from math import *
import numpy


def s(h,k):
    result = 0
    for r in range(1,k):
        result += (r/k) * ((h*r/k) - floor(h*r/k) - 1/2)
    return result


def A_k_n(k,n):
    # result = 0
    # for h in range(k):
    #     if gcd(h,k)== 1:
    #         result += complex(cos(pi*s(h,k)), sin(pi*s(h,k)))/complex(cos(2*pi*n*h/k), sin(2*pi*n*h/k))
    # return result
    if k <= 1:
        return k
    elif k==2:
        return (-1)**n
    s, r, m = 0, 2, n%k
    for l in range(2*k):
        if m == 0:
            s += ((-1)**l)*cos(pi*((6*l+1)/(6*k)))
        m += r
        if m >= k:
            m -= k 

def p(n):
    result = 0
    c = 1/(pi*sqrt(2))
    nn = sqrt(n-(1/24))
    A = [A_k_n(_,n) for _ in range(4*n+1)]
    for k in range(1,4*n):
        result += A[k] * sqrt(k)*(9*pi*cosh(4*pi*nn/(9*k))/(9*k) - sinh(4*pi*nn/(9*k))/(2*nn)/(nn**2))
    return result * c
print(p(91))