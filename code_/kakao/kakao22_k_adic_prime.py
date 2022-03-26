def solution(n, k):
    import math
    def primechk(p): # 소수 판별 함수
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
    digit = int(math.log(n, k)) + 1 # k진수 자리수 구하기
    knumber = [0] * (digit+2) # 양 끝에 0을 추가해서 리스트로 k진수 표현
    for i in range(digit): # 자리수만큼 순회
        knumber[digit -i] = n%k # 처음과 끝을 제외한 자리에 맨 뒤부터 n을 k로 나눈 나머지를 저장
        n = n//k # 그후 n을 k로 나눈 몫으로 교체
    for j in range(digit): # 판별할 수의 앞자리 인덱스 (리스트 knumber 상에서는 실제로는 1 더한 값을 인덱스로 사용)
        for k in range(j,digit): # 판별할 수의 뒷자리 인덱스
            if knumber[j+1] != 0 and knumber[k+1]%4 != 0 and knumber[k+2] == 0 and knumber[j] == 0:
                # 만약 수의 시작부분(j+1)이 0이 아니고 끝자리(k+1)가 4의 배수가 아닌 경우
                # 그리고 시작의 전부분과 끝자리의 뒷부분은 0인 경우
                num = 0
                for d in range(k-j+1): # j+1 부터 k+1까지 값을 쭉 연결한 수를 그대로 10진수로 생각한다.
                    if knumber[k+1-d] == 0: # 각 자리수를 10진수로 합치는 과정에서 0이 나오면 그대로 break
                        break
                    num += knumber[k+1-d] * (10**d)
                else: # break 없이 for문이 완료되면 소수 체크를 한다.
                    if primechk(num):
                        answer += 1
    return answer