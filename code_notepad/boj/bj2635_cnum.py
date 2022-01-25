N = int(input())
# 정수로 input값을 받습니다.
M = round(N*(-1+(5**(1/2)))/2)
# 주어진 수열의 고유방정식을 이용해서 가장 적절한 2번째 값의 근사값을 구합니다.
#정수값으로 계산해야하므로 오차를 고려하여 +-1 범위 내의 경우를 모두 구해봅니다. 
result = []
for idx in range(3):
    seq1 = N # 초기값
    seq2 = M-1+idx # 2번째값+오차범위
    seqs = [seq1, seq2] # 1,2번째와 이후 수열값을 저장할 리스트
    seq = seq1 - seq2 # 3번째 값
    while seq >= 0: # 수열 값이 음수가 되면 종료합니다.
        seqs.append(seq)  #seqs 리스트에 새로운 값 저장
        seq1 = seq2
        seq2 = seq
        seq = seq1 - seq2
        # seq1, seq2, seq에 각각 다음 값들을 저장
    result.append(seqs)
result.sort(key=len)
# 최종적으로 수열의 리스트를 모은 리스트에 대해 len함수(수열 길이)를 기준으로 정렬합니다.
print(len(result[-1]))
# 정렬 후 맨 마지막(가장 길이가 긴) 리스트의 길이를 출력합니다.
print(*result[-1])
# 그 리스트의 내용을 출력합니다.