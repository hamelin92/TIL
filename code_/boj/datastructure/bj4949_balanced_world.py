import sys

def balancer(sentence):
    stack = []
    for s in sentence:
        if s == "[":
            stack.append("[")
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return "no"
        elif s == "(":
            stack.append("(")
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return "no"
    if stack:
        return "no"
    return "yes"


while True:
    sentence = sys.stdin.readline()
    if len(sentence) <= 2:
        break
    print(balancer(sentence))
