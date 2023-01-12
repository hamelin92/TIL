from collections import defaultdict


word = input().upper()
cnt = defaultdict(int)
for w in word:
    cnt[w] += 1
cnt_list = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
if len(cnt) > 1 and cnt_list[0][1] == cnt_list[1][1]:
    print("?")
else:
    print(cnt_list[0][0])
