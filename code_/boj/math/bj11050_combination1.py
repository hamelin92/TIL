def my_combination(n, r):
    factor = 1
    denominator = 1
    for k in range(min(r, n-r)):
        factor *= n-k
        denominator *= k+1
    return factor//denominator

N, K = map(int, input().split())
print(my_combination(N, K))
