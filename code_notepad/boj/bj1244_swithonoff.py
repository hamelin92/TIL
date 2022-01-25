N = int(input())
switchs = list(map(int,input().split()))
people = int(input())
for idx in range(people):
    gender, number = map(int, input().split())
    if gender == 1:
        swt = number
        while swt-1 < N:
            switchs[swt-1] = (switchs[swt-1]+1)%2
            swt += number
    else:
        switchs[number-1] = (switchs[number-1]+1)%2
        swt = 1
        while (number-swt-1 >= 0) and (number+swt-1 < N):
            if switchs[number-swt-1] == switchs[number+swt-1]:
                switchs[number-swt-1] = (switchs[number-swt-1]+1)%2
                switchs[number+swt-1] = (switchs[number+swt-1]+1)%2
                swt += 1
            else:
                break
a = 0
b = 20
while a < len(switchs):
    print(*switchs[a:b])
    a = b
    b += 20