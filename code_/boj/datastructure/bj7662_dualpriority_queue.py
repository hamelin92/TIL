import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    ops = [False for _ in range(k+1)]
    minque, maxque = [], []
    for i in range(k):
        inputs = sys.stdin.readline().split()
        if inputs[0] == "I":
            heapq.heappush(minque, (int(inputs[1]), i))
            heapq.heappush(maxque, (-int(inputs[1]), i))
            ops[i] = True
        else:
            if inputs[1] == "-1":
                while minque and not ops[minque[0][1]]:
                    heapq.heappop(minque)
                if minque:
                    ops[minque[0][1]] = False
                    heapq.heappop(minque)
            else:
                while maxque and not ops[maxque[0][1]]:
                    heapq.heappop(maxque)
                if maxque:
                    ops[maxque[0][1]] = False
                    heapq.heappop(maxque)
    while minque and not ops[minque[0][1]]:
        heapq.heappop(minque)
    while maxque and not ops[maxque[0][1]]:
        heapq.heappop(maxque)
    if minque or maxque:
        print(-maxque[0][0], minque[0][0])
    else:
        print("EMPTY")
