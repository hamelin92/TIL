n = int(input())
seq = [int(input()) for _ in range(n)]
numbers = list(range(1, n+1))
stack = []
result = []
answer = []
flag = True
i = 0
for s in seq:
    while i < n and (not stack or stack[-1] != s):
        stack.append(numbers[i])
        answer.append("+")
        i += 1
    if stack[-1] == s:
        result.append(stack.pop())
        answer.append("-")
    else:
        flag = False
        break
if flag:
    for p in answer:
        print(p)
else:
    print("NO")
