##소수 관련 함수들. 소인수분해


def prime_dic(a):
    b=0
    prime_list={1:2}
    ky=2
    if a==1:
        result={}
    else:
        for d in range(3, int(a) + 1):
            for e in prime_list.values():
                if d % e == 0:
                    b = b + 1
                    break
            if b == 0:
                prime_list[ky] = d
                ky = ky + 1
            else:
                b = 0
        result=prime_list
    return result

def factor_dic(a):
    y=int(a)
    z=int(y**(1/2))
    factor_list={1:1}
    for factor in range(2, z+1):
        fact_ord=0
        for k in range(2, z+1):
            if y % factor == 0:
                y= y / factor
                fact_ord=fact_ord+1
            elif fact_ord >= 1:
                factor_list[factor]=fact_ord
                break
            elif factor > y**(1/2)+1 and y> factor:
                factor_list[int(y)] = 1
                break
            else:
                break
        if y<2:
            break
    result=factor_list
    return result

lis=factor_dic(100005)
lis2=factor_dic(100000002)
print(lis)
print(lis2)