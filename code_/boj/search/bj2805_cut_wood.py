N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort(reverse=True)
break_pts = [0] + heights[:]
for i in range(1, N):
    break_pts[i] = break_pts[i] - break_pts[i+1]
for i in range(1, N):
    break_pts[i+1] = (i+1) * break_pts[i+1] + break_pts[i]
pointer = N//2
left, right = 0, N-1
while left <= right:
    pointer = (left + right) // 2
    if break_pts[pointer+1] > M >= break_pts[pointer]:
        break
    elif break_pts[pointer] > M:
        right = pointer-1
    else:
        left = pointer+1
remainder = M - break_pts[pointer]
max_h = heights[pointer] - remainder//(pointer+1)
if remainder%(pointer+1):
    max_h -= 1
print(max_h)
