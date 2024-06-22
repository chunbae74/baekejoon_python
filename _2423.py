# https://www.acmicpc.net/problem/2423
# 테스트케이스: https://www.acmicpc.net/board/view/43290

### 24.6.22 맞왜틀?
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

Y, X = map(int, input().split())

dist = [[INF] * X for _ in range(Y)]
graph = [[-1] * X for _ in range(Y)]
visited = [[False] * X for _ in range(Y)]

for y in range(Y):
    l = input()
    for x in range(X):
        graph[y][x] = l[x]

if graph[0][0] == "\\":
    dist[0][0] = 0
elif graph[0][0] == "/":
    dist[0][0] = 1
    graph[0][0] = "\\"

d = deque()
d.append([0, 0])

while d:
    nowX, nowY = d.popleft()

    if nowX == X - 1 and nowY == Y - 1:
        break

    for i in range(8):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]

        if 0 <= nextX < X and 0 <= nextY < Y:
            if visited[nextY][nextX]:
                continue

            # 북서
            if dx[i] == -1 and dy[i] == -1:
                if graph[nowY][nowX] == graph[nextY][nextX] and graph[nowY][nowX] == "\\":
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            # 북
            elif dx[i] == 0 and dy[i] == -1:
                if graph[nowY][nowX] != graph[nextY][nextX]:
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            # 북동
            elif dx[i] == 1 and dy[i] == -1:
                if graph[nowY][nowX] == graph[nextY][nextX] and graph[nowY][nowX] == "/":
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    continue

            # 서
            elif dx[i] == -1 and dy[i] == 0:
                if graph[nowY][nowX] != graph[nextY][nextX]:
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            # 동
            elif dx[i] == 1 and dy[i] == 0:
                if graph[nowY][nowX] != graph[nextY][nextX]:
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            # 서남
            elif dx[i] == -1 and dy[i] == 1:
                if graph[nowY][nowX] == graph[nextY][nextX] and graph[nowY][nowX] == "/":
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    continue

            # 남
            elif dx[i] == 0 and dy[i] == 1:
                if graph[nowY][nowX] != graph[nextY][nextX]:
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            # 동남
            elif dx[i] == 1 and dy[i] == 1:
                if graph[nowY][nowX] == graph[nextY][nextX] and graph[nowY][nowX] == "\\":
                    if dist[nextY][nextX] > dist[nowY][nowX]:
                        dist[nextY][nextX] = dist[nowY][nowX]
                        d.appendleft([nextX, nextY])
                else:
                    if dist[nextY][nextX] > dist[nowY][nowX] + 1:
                        dist[nextY][nextX] = dist[nowY][nowX] + 1
                        graph[nextY][nextX] = "/" if graph[nextY][nextX] == "\\" else "\\"
                        d.append([nextX, nextY])

            visited[nextY][nextX] = True

    '''
    for y in range(Y):
        for x in range(X):
            if dist[y][x] == INF:
                print("-", end= " ")
            else:
                print(dist[y][x], end= " ")
        print()

    print("nowX =", nowX, "nowY =", nowY, "\n", "-" * 10)
    '''

print("NO SOLUTION" if graph[Y - 1][X - 1] == "/" else dist[Y - 1][X - 1])
