while True:
    edges = list(map(int, input().split()))
    if not edges[0] and not edges[1] and not edges[2]:
        break
    edges.sort()
    if edges[2] ** 2 == edges[1]**2 + edges[0] ** 2:
        print("right")
    else:
        print("wrong")