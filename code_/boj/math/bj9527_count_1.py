import sys
sys.setrecursionlimit(100000)
A, B = map(int, input().split())

def count_num(a, b):
    val = 0
    if a > b:
        return 0
    if a == b:
        while a > 0:
            while a%2 == 0:
                a //= 2
            a -= 1
            val += 1
        return val
    val += (b-a-(a+1)%2-(b+1)%2)//2 + 1
    if a%2:
        val += count_num(a-1, a-1)
    if b%2 == 0:
        val += count_num(b, b)
    return val + 2*count_num(max((a+1)//2, 1), (b-1)//2)

ans = count_num(A, B)
print(ans)