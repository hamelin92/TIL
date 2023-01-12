N = int(input())
scores = list(map(int, input().split()))
max_score = 0
sum_of_score = 0
for i in range(N):
    sum_of_score += scores[i]
    if scores[i] > max_score:
        max_score = scores[i]
print(f"{(sum_of_score*100)/(max_score * N)}")
