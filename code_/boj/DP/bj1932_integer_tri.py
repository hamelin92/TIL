n = int(input())
tri_sums = [0] * (n+1)
for i in range(n):
    row = list(map(int, input().split()))
    for i in range(len(row)-1,0,-1):
        tri_sums[i] = max(tri_sums[i], tri_sums[i-1]) + row[i]
    tri_sums[0] += row[0]
print(max(tri_sums))
