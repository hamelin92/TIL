import math

T = int(input())
for tc in range(1, T+1):
    A, B, K = map(int, input().split())
    d = math.gcd(A,B)
    turn = 0
    a = A//d
    b = B//d
    candies = [a, b]
    for i in range(K):
        if candies[0] == 0 or candies[1] == 0:
            break
        elif candies[0] == 1:
            break
        dd = math.gcd(candies[0], candies[1])
        d *= dd
        candies[0] //= dd
        candies[1] //= dd
        candies[1] += candies[0]
        candies[0] <<= 1
        candies[1] -= candies[0]
        candies.sort()
    print(f'#{tc} {d*min(candies)}')


'''
1
956657 720636341 100000000
4
4 9 1
4 9 2
4 9 3
500 2000 2000000000
'''
