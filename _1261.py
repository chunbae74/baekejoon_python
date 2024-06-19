# 1261
from collections import deque

INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 가로 M, 세로 N
M, N = map(int, input().split())
dist = [[INF] * M for _ in range(N)]
graph = [[0] * M for _ in range(N)]

for i in range(N):
    l = input()
    for j in range(M):
        graph[i][j] = int(l[j])

# 출발지 초기화
dist[0][0] = 0
d = deque([[0, 0]])
while d:
    nowX, nowY = d.popleft()

    for i in range(4):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]

        # 범위 내
        if 0 <= nextX < N and 0 <= nextY < M:
            if dist[nowX][nowY] + graph[nextX][nextY] < dist[nextX][nextY]:
                dist[nextX][nextY] = dist[nowX][nowY] + graph[nextX][nextY]
                # 간선 비용이 0이라면 앞에 추가
                if graph[nextX][nextY]:
                   d.append([nextX, nextY])
                else:
                    d.appendleft([nextX, nextY])

print(dist[N - 1][M - 1])