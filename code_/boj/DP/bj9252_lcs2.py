first_str = list(input())
second_str = list(input())
lcs = [[""] * (len(second_str)+1) for _ in range(len(first_str)+1)]
max_subseq = ""
for i in range(1, len(first_str)+1):
    for j in range(1, len(second_str)+1):
        if first_str[i-1] == second_str[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + first_str[i-1]
            if len(lcs[i][j]) > len(max_subseq):
                max_subseq = lcs[i][j]
        else:
            if len(lcs[i-1][j]) > len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
print(len(max_subseq))
print(max_subseq)
