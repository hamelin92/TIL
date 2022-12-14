M = int(input())
factors = []
N_fact = M
for j in range(2, int(M ** (1/2))+1):
    if N_fact%j == 0:
        factor = [j, 0]
        while N_fact%j == 0:
            N_fact = N_fact//j
            factor[1] += 1
        factors.append(factor)
else:
    if N_fact > 1:
        factors.append([N_fact, 1])
a = M//3
ar = M%3
A = [a, a, 1, 1]
if ar > 0:
    A[0] += 1
    A[1] += 1
if (M - 4)%3 == 0:
    A[0] -= 1
b = 0
b2 = 0
for f in factors:
    if f[0] == 2:
        b2 = f[1]
    b += f[1]
if b:
    A[2] = b - b2//2
    A[3] = b
print(str(A).replace("[", "").replace("]", "").replace(",", ""))