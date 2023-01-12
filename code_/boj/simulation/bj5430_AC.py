from collections import deque

def AC(p, arr):
    deq = deque(arr)
    sign = True
    for op in func:
        if op == "D":
            if not deq:
                return "error"
            if sign:
                deq.popleft()
            else:
                deq.pop()
        if op == "R":
            sign = not sign
    if sign:
        return str(list(deq)).replace(" ", "")
    return str(list(deq)[::-1]).replace(" ", "")


for t in range(int(input())):
    func = input()
    n = int(input())
    nums = list(map(int, filter(lambda x: x.isnumeric(), input().replace("[", "").replace("]","").split(","))))
    print(AC(func, nums))
