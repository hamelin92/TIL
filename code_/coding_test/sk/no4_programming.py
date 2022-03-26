def solution(n, edges):
    answer = 0
    graph = [[0]*n for _ in range(n)] # 그래프를 n*n 행렬로 나타내기
    for edge in edges: # 방향이 없는 연결 그래프를 2차 리스트(행렬)로 나타내기
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    for i in range(n-1):#1부터 n-2까지
        for j in range(i+1, n):#i부터 n-1까지
            # 이렇게 해서 모든 서로 다른 노드의 쌍 조합을 구할 수 있다.
            visited = [0] * n # DFS 알고리즘을 쓰기 위한 초기 세팅
            visited[i] = 1
            stack = [i]
            while True: # DFS 알고리즘 사용
                for k in range(n):
                    if graph[stack[-1]][j] == 1:
                        visited[j] = 1
                        stack.append(j)
                        break
                    elif graph[stack[-1]][k] == 1 and visited[k] == 0:
                        # 방문 기록이 없는 노드는 스택에 넣고 방문기록에 넣는다.
                        visited[k] = 1
                        stack.append(k)
                        break
                else: # 갈 곳이 없는 경우 pop을 한다.
                    stack.pop()
                if len(stack) == 0: # 만약 스택이 비면 while문을 종료한다.
                    break
                elif stack[-1] == j: # 만약 가장 최근에 j값을 방문했다면 while문을 종료한다.
                    break
            if len(stack) > 2: # 만약 stack에 2개를 초과한 원소가 있다면 answer에 값을 계산해서 더해준다.
                answer += 2 * (len(stack) - 2)
                # 문제에서 말하고 있는 순서쌍 (i, j, k) 조건을 충족시키려면 j가 i와 k 사이의 최단경로 내에 존재해야한다는 것이다.
                # 앞서 for문으로 구한 i,j 조합을 문제에서 순서쌍의 양끝으로 하고 그외의 stack의 원소는 i와 j 사이에 들어갈 수 있는 후보이다.
                # stack의 i,j가 아닌 임의의 원소를 x 라고 할 때 (i, x, j), (j, x, i) 두 순서쌍은 문제의 조건을 충족시키게 된다.
                # 그러므로 x가 될 수 있는 것은 stack 전체에서 i,j만 제외한 것이므로 [ len(stack) - 2 ]
                # i와 j의 순서는 바꿔도 상관이 없으므로 거기에 2를 곱해준다. 그것을 answer 값에 누적시킨다.
    return answer

print(solution(6, [[0,1],[0,2],[0,5],[1,3],[1,4]]))


'''
문제 설명
n개의 노드로 이루어진 트리가 있습니다. 각 노드에는 0번부터 n-1번까지 번호가 매겨져 있습니다. 이때, 당신은 다음 조건을 모두 만족하는 정수 순서쌍 (i,j,k)의 개수를 구하고자 합니다.

0 ≤ i, j, k < n
i, j, k는 서로 다릅니다.
distance(a, b)를 a번 노드와 b번 노드를 잇는 경로 상의 간선의 개수라고 할 때, distance(i, j) + distance(j, k) = distance(i, k)입니다.
트리의 노드 개수를 의미하는 n과 간선 정보가 담긴 2차원 정수 배열 edges가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 순서쌍 (i,j,k)의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ n ≤ 300,000
edges의 행의 개수 = n - 1
edges의 각 행은 [v1,v2] 2개의 정수로 이루어져 있으며, 이는 v1번 노드와 v2번 노드 사이에 간선이 있음을 의미합니다.
0 ≤ v1 < n
0 ≤ v2 < n
v1 ≠ v2
edges가 의미하는 그래프가 항상 트리인 경우만 입력으로 주어집니다.
입출력 예
n	edges	result
5	[[0,1],[0,2],[1,3],[1,4]]	16
4	[[2,3],[0,1],[1,2]]	8
입출력 예 설명
입출력 예 #1

다음 그림은 입력으로 주어진 트리를 나타낸 것입니다.
ex1.png

다음 표는 입력으로 주어진 트리에서 문제의 조건을 모두 만족하는 순서쌍의 목록을 나타낸 것입니다.
i	j	k	distance(i, j)	distance(j, k)	distance(i, k)
0	1	3	1	1	2
0	1	4	1	1	2
1	0	2	1	1	2
2	0	1	1	1	2
2	0	3	1	2	3
2	0	4	1	2	3
2	1	3	2	1	3
2	1	4	2	1	3
3	0	2	2	1	3
3	1	0	1	1	2
3	1	2	1	2	3
3	1	4	1	1	2
4	0	2	2	1	3
4	1	0	1	1	2
4	1	2	1	2	3
4	1	3	1	1	2
문제의 조건을 모두 만족하는 순서쌍이 16개이므로, 16을 return 해야 합니다.
입출력 예 #2

다음 그림은 입력으로 주어진 트리를 나타낸 것입니다.
ex2.png

다음 표는 입력으로 주어진 트리에서 문제의 조건을 모두 만족하는 순서쌍의 목록을 나타낸 것입니다.
i	j	k	distance(i, j)	distance(j, k)	distance(i, k)
0	1	2	1	1	2
0	1	3	1	2	3
0	2	3	2	1	3
1	2	3	1	1	2
2	1	0	1	1	2
3	1	0	2	1	3
3	2	0	1	2	3
3	2	1	1	1	2
문제의 조건을 모두 만족하는 순서쌍이 8개이므로, 8을 return 해야 합니다.
'''