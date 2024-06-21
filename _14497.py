# https://www.acmicpc.net/problem/14497
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

Y, X = map(int, input().split())
dist = [[INF] * X for _ in range(Y)]
graph = [[-1] * X for _ in range(Y)]

# (x1, y1) : 주난이의 위치
# (x2, y2) : 범인의 위치
y1, x1, y2, x2 = map(int, input().split())

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

for y in range(Y):
    l = input()
    for x in range(X):
        if l[x] == "#" or l[x] == "*":
            graph[y][x] = 0
        else:
            graph[y][x] = int(l[x])

# 시작지점
dist[y1][x1] = 1

d = deque([[x1, y1]])
while d:
    nowX, nowY = d.popleft()

    for i in range(4):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]

        if 0 <= nextX < X and 0 <= nextY < Y:
            if dist[nowY][nowX] + graph[nextY][nextX] < dist[nextY][nextX]:
                dist[nextY][nextX] = dist[nowY][nowX] + graph[nextY][nextX]

                if graph[nextY][nextX] == 0:
                    d.appendleft([nextX, nextY])
                else:
                    d.append([nextX, nextY])

print(dist[y2][x2])