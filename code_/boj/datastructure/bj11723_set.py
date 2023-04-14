import sys

S = {x: 0 for x in range(1, 21)}

def setadd(x):
    S[x] = 1

def setremove(x):
    S[x] = 0

def check(x):
    print(S[x])

def toggle(x):
    S[x] = int(not S[x])

def all(x):
    for k in range(1,21):
        S[k] = 1

def empty(x):
    for k in range(1,21):
        S[k] = 0

operations = {
    "add": setadd,
    "remove": setremove,
    "check": check,
    "toggle": toggle,
    "all": all,
    "empty": empty
}
M = int(sys.stdin.readline())
for _ in range(M):
    ops = sys.stdin.readline().split()
    if len(ops) >= 2:
        ops[-1] = int(ops[-1])
    operations[ops[0]](ops[-1])
