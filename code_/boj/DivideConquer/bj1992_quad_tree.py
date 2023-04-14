import sys
N = int(sys.stdin.readline())
image = [list(map(int, list(sys.stdin.readline().strip("\n")))) for _ in range(N)]


def compress(img):
    n = len(img)
    sn = n//2
    val = sum(img[0])
    if sum(img[0])%n == 0:
        for i in range(1, n):
            if sum(img[i]) != val:
                break
        else:
            return int(bool(val))
    q_tree = []
    for i in range(2):
        for j in range(2):
            q_tree.append([img[i*sn+k][j*sn:(j+1)*sn] for k in range(sn)])
    return list(map(compress, q_tree))


print(str(compress(image)).replace("[", "(").replace("]", ")").replace(", ", ""))

