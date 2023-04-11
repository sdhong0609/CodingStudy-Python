""" P.152 미로 탈출 """

""" 내 풀이 """
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    count = 1
    queue = deque([(x, y)])
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                count += 1
                graph[nx][ny] = count


bfs(0, 0)

print(graph[n - 1][m - 1])

# 입력 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 1
# 10

# 입력 2
# 3 3
# 110
# 010
# 011

# 출력 2
# 5
