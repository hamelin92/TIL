def powers(A,B):
    global P
    A = D = A%P
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2

    for exp in seq[::-1]:
        if exp:
            A = (A ** 2) * D
        else:
            A = (A ** 2)
        A = A%P
    return A if B > 0 else 1


N, P = map(int, input().split())
a = list(map(int, input().split()))[::-1]
reduc = [sum(a[i::P-1])%P if i > 0 else a[0]%P for i in range(P)]
length = min(N+1, P)
print(reduc[0])
for i in range(1,P-1):
    print(sum([powers(i, s)*reduc[s] for s in range(length)])%P)
print((sum(reduc[::2])-sum(reduc[1::2]))%P)
