import sys
N, M = map(int, sys.stdin.readline().split())
poke_dict = {}
for i in range(1, N+1):
    poke = sys.stdin.readline().strip("\n")
    poke_no = str(i)
    poke_dict[poke] = poke_no
    poke_dict[poke_no] = poke
ans = [poke_dict[sys.stdin.readline().strip("\n")] for _ in range(M)]
print(*ans, sep="\n")