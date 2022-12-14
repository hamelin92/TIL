from math import gcd

W = int(input())
for w in range(W):
    p, q, n = map(int, input().split())
    p %= q
    d = gcd(p, q)
    p_r = p//d
    q_r = q//d
    m = n//q_r
    n = n%q_r
    S = 0
    if m > 0:
        S += (d*m) * (q_r*(q_r-1)//2)
    q_rr = q_r//p_r
    q_recip = q_r%p_r
    p_rr = p_r//q_recip
    mul = n//q_rr
    re = n%q_rr
    s = 0
    cnt = mul//p_rr
    for cnt in range(mul):
        s += p_r*(cnt*q_rr+1)%q_r
    
    S += s*d*q_rr
    S+=d*(p_r*re*(re+1)//2+(p_r*(mul*q_rr+1)%q_r-p_r)*re) + mul*d*p_r*q_rr*(q_rr+1)//2 - p_r*q_rr*mul
    print(S)

