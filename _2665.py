# https://www.acmicpc.net/problem/2665
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
dist = [[INF] * N for _ in range(N)]
graph = [[0] * N for _ in range(N)]

for i in range(N):
    l = input()
    for j in range(N):
        num = int(l[j])
        graph[i][j] = 1 if num == 0 else 0

dist[0][0] = 0
d = deque([[0, 0]])
while d:
    nowX, nowY = d.popleft()

    for i in range(4):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]

        if 0 <= nextX < N and 0 <= nextY < N:
            if dist[nowX][nowY] + graph[nextX][nextY] < dist[nextX][nextY]:
                dist[nextX][nextY] = dist[nowX][nowY] + graph[nextX][nextY]
                if graph[nextX][nextY] == 0:
                    d.appendleft([nextX, nextY])
                else:
                    d.append([nextX, nextY])

print(dist[N - 1][N - 1])