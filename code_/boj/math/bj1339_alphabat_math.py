from collections import defaultdict

N = int(input())
words = [input() for _ in range(N)]
w_values = defaultdict(int)
numbers = list(range(10))
for word in words:
    length = len(word)
    for i in range(length):
        w_values[word[i]] += 10**(length-i-1)

sorted_values = sorted(w_values.items(), key=lambda x: x[1], reverse=True)
ans = 0
for i in range(len(sorted_values)):
    ans += sorted_values[i][1] * numbers[9-i]
print(ans)