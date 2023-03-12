def div_conq(row, col, s, dim):
    if dim <= 2:
        return 2*row + col + s
    subdim = dim//2
    return div_conq(row%subdim, col%subdim, s+(2*(row//subdim)+(col//subdim))*(subdim**2), subdim)

N, r, c = map(int, input().split())
ndim = 1<<N
print(div_conq(r, c, 0, ndim))
