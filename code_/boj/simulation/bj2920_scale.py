def determine(seq):
    if seq[0] == 1:
        start = [1, "ascending"]
    elif seq[0] == 8:
        start = [-1, "descending"]
    else:
        return "mixed"
    for i in range(1, 8):
        if seq[i] - seq[i-1] == start[0]:
            continue
        else:
            return "mixed"
    return start[1]


scales = list(map(int, input().split()))
print(determine(scales))
