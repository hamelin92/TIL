N = int(input())
area = 0
origin_x, origin_y = map(int, input().split())
first_x, first_y = origin_x, origin_y
for n in range(N-1):
	second_x, second_y = map(int, input().split())
	area += first_x * second_y - first_y * second_x
	first_x, first_y = second_x, second_y
else:
	area += first_x * origin_y - first_y * origin_x
print(abs(round(area/2, 1)))
