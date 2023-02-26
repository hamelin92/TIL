N = int(input())
for n in range(N):
    ps = input()
    check = 0
    for w in ps:
        if w == "(":
            check += 1
        elif check == 0:
            check -= 1
            break
        else:
            check -= 1
    if check:
        print("NO")
    else:
        print("YES")