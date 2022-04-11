def solution(s):
    s = list(s)
    l = len(s)
    result = []
    for k in range(1,l//2+2):
        tmp_l = l%k
        multiplicity = [0]*(l//k)
        idx = 0
        part = s[0:k]
        for i in range(l//k):
            if part != s[i*k:(i+1)*k]:
                part = s[i*k:(i+1)*k]
                idx = i
                multiplicity[idx] = 1
            else:
                multiplicity[idx] +=1
        for j in multiplicity:
            if j > 1:
                dig = 0
                while j:
                    j = j//10
                    dig += 1
                tmp_l += k+dig
            else:
                tmp_l += k * j
        result.append(tmp_l)
    answer = min(result)
    return answer
solution("abcabcabcabcdededededede")

'''
s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17

'''