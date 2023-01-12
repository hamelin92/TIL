A = int(input())
B = int(input())
C = int(input())
cnt = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
n = str(A*B*C)
for a in n:
    cnt[a] += 1
for v in cnt.values():
    print(v)
