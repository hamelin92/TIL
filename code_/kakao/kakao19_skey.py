def solution(relation):
    from itertools import combinations
    n = len(relation)
    r = len(relation[0])
    keys = []
    for k in range(1,r+1):
        for cb in combinations(range(r),k):
            for key in keys:
                if key.issubset(set(cb)):
                    break
            else:
                rec = set()
                for rel in relation:
                    rec.add(tuple([rel[i] for i in cb]))
                if len(rec) == n:
                    keys.append(set(cb))
    answer = len(keys)
    return answer

solution([
["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]
])


'''
relation	result
[
["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]
]
2
'''