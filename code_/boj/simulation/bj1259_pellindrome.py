import sys

while True:
    w = sys.stdin.readline().strip("\n")
    if w == "0":
        break
    n = len(w)
    for i in range(n//2):
        if w[i] != w[n-1-i]:
            print("no")
            break
    else:
        print("yes")