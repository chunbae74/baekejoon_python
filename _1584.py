# https://www.acmicpc.net/problem/1584
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maxLen = 501

dist = [[INF] * maxLen for _ in range(maxLen)]
# -1: 죽음 구역
#  1: 위험 구역
#  0: 안전 구역
graph = [[0] * maxLen for _ in range(maxLen)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y1 > y2:
        tmp = y1
        y1 = y2
        y2 = tmp

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            graph[y][x] = 1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y1 > y2:
        tmp = y1
        y1 = y2
        y2 = tmp

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            graph[y][x] = -1

dist[0][0] = 0
d = deque()
d.append([0, 0])
while d:
    nowX, nowY = d.popleft()

    for i in range(4):
        nextX, nextY = nowX + dx[i], nowY + dy[i]
        if 0 <= nextX < maxLen and 0 <= nextY < maxLen:
            # 죽음지역은 갈 수 없음
            if graph[nextY][nextX] == -1:
                continue

            if dist[nextY][nextX] > dist[nowY][nowX] + graph[nextY][nextX]:
                dist[nextY][nextX] = dist[nowY][nowX] + graph[nextY][nextX]
                if graph[nextY][nextX] == 0:
                    d.appendleft([nextX, nextY])
                else:
                    d.append([nextX, nextY])

print("-1" if dist[500][500] == INF else dist[500][500])
