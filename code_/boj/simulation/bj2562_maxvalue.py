max_val = [0, 0]
for i in range(1, 10):
    n = int(input())
    if max_val[0] < n:
        max_val = [n, i]
print(max_val[0])
print(max_val[1])
