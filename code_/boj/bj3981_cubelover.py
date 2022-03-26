import math
T = int(input())
for _ in range(T):
    n, *x = map(int, input().split())
    if len(x) < 4:
        print('YES')
    else:
        a = (-x[0]+3*x[1]-3*x[2]+x[3])/6
        b = (9*x[0]-24*x[1]+21*x[2]-6*x[3])/6
        c = (-26*x[0]+57*x[1]-42*x[2]+11*x[3])/6
        d = (24*x[0]-36*x[1]+24*x[2]-6*x[3])/6
        for idx in range(len(x)):
            if math.isclose(a*(idx+1)**3 + b*(idx+1)**2 + c*(idx+1) + d, x[idx]) is False:
                print('NO')
                break
            else:
                continue
        else:
            print('YES')