def solution(k, m, names, amounts):
    answer = 0
    name_up = list(map(lambda x: x.upper(), names)) # 비교하기 수월하도록 이름을 전부 대문자로 변경
    N = len(name_up)
    last_name = name_up[0] # 가장 마지막에 송금한 사람 체크 (연속성 확인)
    repeat = 0 # 연속 횟수 초기값 ( 시작 전 0 후 1)
    for i in range(N):
        if last_name == name_up[i]: # 연속적인 경우 repeat 1 증가
            repeat += 1
        else:
            last_name = name_up[i] # 연속이 깨진 경우 last_name을 갱신하고 repeat 변수도 1로 갱신
            repeat = 1
        if repeat >= k: # 만약 k 이상 연속했을 시 answer +1
            answer += 1
        elif amounts[i] >= m: # 위 조건이 아닌 경우 만약 m원 이상 송금시 answer +1 (두가지 경우가 동시에 발생한 경우 중복 체크 되는 것을 회피)
            answer += 1
    return answer




'''
문제 설명
어떤 은행에서는 고객들이 송금할 때, 다음의 두 가지 조건 중 한 가지 이상 해당하면 보이스피싱 주의 문자를 발송합니다.

[문자 발송 조건]

같은 사람에게 k번 이상 연속으로 송금할 때
사람 이름을 비교할 때, 대소문자는 구분하지 않습니다.
송금액이 m원 이상일 때
아래의 표는 k = 3, m = 50000 인 경우에 고객들의 송금 내역에 따른 문자 발송 결과입니다.

받는 사람 이름	송금액	결과
msLEE	950
jsKim	52524	송금액이 50000원 이상이므로, 문자 발송
jsKIM	1400
jskiM	6055	3번 연속으로 같은 사람에게 송금하므로, 문자 발송
jskim	10000	4번 연속으로 같은 사람에게 송금하므로, 문자 발송
John	4512
john	512
John	52000	두 가지 조건 모두 해당하므로, 문자 발송
msLEE	9000
msLEE	49000
jsKIM	1400
roy	50000	송금액이 50000원 이상이므로, 문자 발송
위의 예시에서는 총 5회 문자가 발송됩니다.
고객들에게 문자를 발송하는 기준이 되는 정수 k와 m, 송금을 받는 사람의 이름을 담은 문자열 배열 names, 송금액을 담은 정수 배열 amounts가 매개변수로 주어집니다. 이때, 문자가 발송되는 횟수를 return 하도록 solution 함수를 완성해주세요. 만약 문자가 한 번도 발송되지 않으면, 0을 return 합니다.

제한사항
2 ≤ k ≤ 10
1 ≤ m ≤ 1,000,000
1 ≤ names의 길이 ≤ 1,000
3 ≤ names의 원소의 길이 ≤ 10
names의 원소는 알파벳 소문자와 알파벳 대문자로만 이루어진 문자열입니다.
amounts의 길이 = names의 길이
1 ≤ amounts의 원소 ≤ 1,000,000
names[i]와 amounts[i]는 i+1 번째 송금 내역에서 받는 사람 이름과 송금액을 의미합니다.
입출력 예
k	m	names	amounts	result
3	50000	["msLEE", "jsKim", "jsKIM", "jskiM", "jskim", "John", "john", "John", "msLEE", "msLEE", "jsKIM", "roy"]	[950, 52524, 1400, 6055, 10000, 4512, 512, 52000, 9000, 49000, 1400, 50000]	5
2	3451	["abcd", "aBCd", "jsKIM", "rrr", "rrr"]	[950, 1000, 1400, 4000, 10000]	3
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다. 총 5회 문자가 발송되므로, 5를 return 합니다.
입출력 예 #2

받는 사람 이름	송금액	결과
abcd	950
aBCd	1000	2회 연속으로 같은 사람에게 송금하므로, 문자 발송
jsKIM	1400
rrr	4000	송금액이 3451원 이상이므로, 문자 발송
rrr	10000	두 가지 조건 모두에 해당하므로, 문자 발송
총 3회 문자가 발송되므로, 3을 return 합니다.

'''