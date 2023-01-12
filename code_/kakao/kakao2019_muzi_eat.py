def solution(food_times, k):
    removed = [0]*len(food_times)
    enum = list(enumerate(food_times, start=0))
    enum.sort(key=lambda x: x[1], reverse=True)
    const = 0
    while enum and (enum[-1][1]-const)*len(enum) <= k:
        last = enum.pop()
        k -= (last[1]-const)*(len(enum)+1)
        removed[last[0]] = 1
        const = last[1]
    if not enum:
        return -1
    ind = k%len(enum)
    filtered = list(filter(lambda x: removed[x] == 0,list(range(len(removed)))))
    return filtered[ind]+1

ft = [8, 5, 4,7,3,1,10,5, 8]
kk = 50

print(solution(ft, kk))