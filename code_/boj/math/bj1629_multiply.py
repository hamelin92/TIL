A, B, C = map(int, input().split())
A = D = A%C

seq = []
while B > 1:
    seq.append(B%2)
    B = B//2

for exp in seq[::-1]:
    if exp:
        A = (A ** 2) * D
    else:
        A = (A ** 2)
    A = A%C
print(A)
