# from collections import defaultdict
import sys
sys.setrecursionlimit(1000001)


def vec_sum(v1, v2):
    global K
    if v1[1]+v2[1] > K:
        return False
    return ((v1[0]+v2[0])%33330, v1[1]+v2[1])


def FFT(dict=, w):


def poly_multiplication(dict1, dict2):
    global K
    ans_dict = {(0,0): 1}
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            new_k = vec_sum(key1, key2)
            if not new_k:
                continue
            if ans_dict.get(new_k) is None:
                ans_dict[new_k] = 0
            ans_dict[new_k] += dict1[key1] * dict2[key2]%99991
    return ans_dict


def subset_sums(num_set):
    l = len(num_set)
    if l <= 1:
        poly = {(0, 0): 1}
        for i in range(l):
            poly[(num_set[i]%33330,1)] = 1
        return poly
    if l == 2:
        poly = {(0,0): 1}
        s = 0
        for i in range(l):
            poly[(num_set[i]%33330,1)] = 1
        poly[(sum(num_set)%3330,2)] = 1
        return poly
    return poly_multiplication(subset_sums(num_set[:l//2]), subset_sums(num_set[l//2:l]))


def multiply(mat1, mat2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result[i][j] = sum([mat2[k][j] * mat1[i][k] for k in range(2)])%99991
    return result


def matpower(mat, B):
    ans = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            ans[i][j] = mat[i][j]
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2
    for exp in seq[::-1]:
        if exp:
            ans = multiply(multiply(ans, ans), mat)
        else:
            ans = multiply(ans, ans)
    return ans

f = [[1, 1], [1, 0]]

# N, K = map(int, input().split())
# S = list(map(int, input().split()))
N = 50000
K = 25000
S = list(range(1, 50001))

print("N= 50, K=25, S=range(1, 51)")
memo_len = min(sum(S[N-K:])+1, 33330)
fibonacci = [0]*memo_len
f_count = [0]*memo_len
fibonacci[1] = 1
for i in range(2, memo_len):
    fibonacci[i] = (fibonacci[i-1] + fibonacci[i-2])%99991


subsets = list(filter(lambda x: x[0][1] == K ,subset_sums(S).items()))
print('subsets ok')
print(len(subsets))
ans = 0
for ss in subsets:
    ans = (ans+fibonacci[ss[0][0]%33330] * ss[1])%99991
print(fibonacci)
