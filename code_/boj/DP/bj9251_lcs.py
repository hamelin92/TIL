first_str = list(input())
second_str = list(input())
lcs = [[0] * (len(second_str)+1) for _ in range(len(first_str)+1)]
max_subseq = 0
for i in range(1, len(first_str)+1):
    for j in range(1, len(second_str)+1):
        if first_str[i-1] == second_str[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            if lcs[i][j] > max_subseq:
                max_subseq = lcs[i][j]
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(max_subseq)
