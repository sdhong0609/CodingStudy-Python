""" P.262 전보 """

""" 내 풀이 """
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)  #

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # (목적지 노드, 거리) 순


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # (거리, 노드) 순
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

distance.remove(0)
distance.remove(INF)
print(len(distance), max(distance))
