""" P.303 커리큘럼 """

""" 내 풀이 """
from collections import deque
import copy

n = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(n + 1)]

time = [0]  # 각 강의 시간
result = []

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time.append(data[0])
    data = data[1:len(data) - 1]
    indegree[i] = len(data)
    for x in data:
        graph[x].append(i)


def topology_sort():
    global result
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        max_time = result[now]
        for i in graph[now]:
            indegree[i] -= 1
            result[i] += max_time
            if indegree[i] == 0:
                q.append(i)


topology_sort()

# 입력
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 출력
# 10
# 20
# 14
# 18
# 17
