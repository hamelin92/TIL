seq = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
T = int(input())
for t in range(T):
    N = int(input())
    while N > len(seq)-1:
        seq.append(seq[-1] + seq[-5])
    print(seq[N])