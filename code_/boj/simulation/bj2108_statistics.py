from collections import defaultdict
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
cnt = defaultdict(int)

for n in nums:
    cnt[n] += 1
extreme_value = max(cnt.values())
arr = []
for k in cnt.keys():
    if cnt[k] == extreme_value:
        arr.append(k)

print(int(round(sum(nums)/N,0)))
print(nums[N//2])
print(arr[1] if len(arr) > 1 else arr[0])
print(nums[-1]-nums[0])
