t = int(input())
for tc in range(t):
    score = 0
    result = input().split("X")
    for o in result:
        l = len(o)
        score += l*(l+1)//2
    print(score)
