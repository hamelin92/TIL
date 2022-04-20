def solution(p):
    answer = ''
    def inverse(s):
        result = ''
        for i in s:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result
    def correct(s):
        chk = 0
        crt = True
        for i in range(len(s)):
            if s[i] == '(':
                chk += 1
            else:
                chk -= 1
            if chk < 0:
                crt = False
            if chk == 0:
                return (i, crt)
    results = []
    stack = []
    s = p
    while len(s):
        k, check = correct(s)
        if check:
            results.append(s[:k+1])
            s = s[k+1:]
        else:
            stack.append(inverse(s[1:k]))
            stack.append(')')
            results.append('(')
            s = s[k+1:]
    for i in results:
        answer += i
    while stack:
        q = stack.pop()
        answer += q
    return answer
solution("()))((()")

'''
"(()())()"	"(()())()"
")("	"()"
"()))((()"	"()(())()"
'''

