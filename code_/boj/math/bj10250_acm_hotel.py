T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    y = (N-1)%H+1
    x = (N-1)//H + 1
    print(100*y+x)