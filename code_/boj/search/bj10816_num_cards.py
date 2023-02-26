import sys
from collections import defaultdict

N = int(sys.stdin.readline())
cards = defaultdict(int)
for num in sys.stdin.readline().split():
    cards[num] += 1
M = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
print(*map(lambda x: cards[x], nums))
