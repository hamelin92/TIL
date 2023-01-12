T = int(input())
for t in range(T-1):
    S = input().split()
    R = int(S[0])
    for w in S[1]:
        print(w*R, end="")
    print()
S = input().split()
R = int(S[0])
for w in S[1]:
    print(w*R, end="")
