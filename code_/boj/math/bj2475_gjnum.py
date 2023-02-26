recip = [0, 1, 4, 9, 6, 5, 6, 9, 4, 1]
print(sum(recip[i] for i in map(int, input().split()))%10)
