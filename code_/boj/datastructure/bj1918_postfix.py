notation = input()
res = []
stack = []
priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}
for s in notation:
    if 65 <= ord(s) <= 90:
        res.append(s)
    elif s == "(":
        stack.append("(")
    elif s == ")":
        while stack and stack[-1] != "(":
            res.append(stack.pop())
        if stack and stack[-1] == "(":
            stack.pop()
    elif s == "+" or s == "*" or s == "-" or s == "/":
        while stack and priority[s] <= priority[stack[-1]]:
            res.append(stack.pop())
        stack.append(s)
while stack:
    res.append(stack.pop())
print(*res, sep="")