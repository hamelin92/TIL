def solution(n, k):
    import math
    def primechk(p):
        if p == 1:
            return False
        elif p == 2:
            return True
        elif p % 2:
            for i in range(3, int(math.sqrt(p)) + 1, 2):
                if p % i == 0:
                    return False
            else:
                return True
        else:
            return False

    answer = 0
    digit = int(math.log(n, k)) + 1
    knumber = [0] * digit
    for i in range(digit):
        knumber[digit -1 -i] = n%k
        n = n//k
    for j in range(digit):
        for k in range(j,digit):
            if j == 0 and k < digit-1 and knumber[j] != 0 and knumber[k]%4 != 0 and knumber[k+1] == 0:
                num = 0
                for d in range(k-j+1):
                    if knumber[k-d] == 0:
                        break
                    num += knumber[k-d] * (10**d)
                else:
                    if primechk(num):
                        answer += 1
            elif j ==0 and k == digit-1 and knumber[j] != 0 and knumber[k]%4 != 0:
                num = 0
                for d in range(k - j + 1):
                    if knumber[k-d] == 0:
                        break
                    num += knumber[k - d] * (10 ** d)
                else:
                    if primechk(num):
                        answer += 1
            elif 0 < j and k < digit-1 and knumber[j] != 0 and knumber[k]%4 != 0 and knumber[j-1] == 0 and knumber[k+1] == 0:
                num = 0
                for d in range(k-j+1):
                    if knumber[k-d] == 0:
                        break
                    num += knumber[k-d] * (10**d)
                else:
                    if primechk(num):
                        answer += 1
            elif 0 < j and k == digit-1 and knumber[j] != 0 and knumber[k]%4 != 0 and knumber[j-1] == 0:
                num = 0
                for d in range(k-j+1):
                    if knumber[k-d] == 0:
                        break
                    num += knumber[k-d] * (10**d)
                else:
                    if primechk(num):
                        answer += 1
    return answer