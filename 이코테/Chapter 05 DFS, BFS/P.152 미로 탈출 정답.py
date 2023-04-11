""" P.152 미로 탈출 정답 """

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))

'''
이미 방문했던 곳의 값이 변경될 수 있지만 맨 우측 하단 값만 요구하고 있기 때문에
답을 도출하는 데에 문제없다.
'''

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
