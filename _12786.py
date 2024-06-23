# https://www.acmicpc.net/problem/12786
# 24.6.22 ㅋㅋ 시발

from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
K = int(input())

# dist: T를 사용한 횟수
dist = [INF] * (N + 1)
graph = []

for i in range(N):
    l = input()
    M = int(l.split()[0])
    arr = []
    for j in range(1, M + 1):
        arr.append(int(l.split()[j]))
    graph.append(arr)

dist[0] = 0
d = deque()
# [idx, preHeight]
d.append([0, 1])
while d:
    nowIdx, nowHeight = d.popleft()

    if nowIdx == N:
        break

    nextIdx = nowIdx + 1
    for nextHeight in graph[nowIdx]:
        # T기능 사용 안해도 될 때
        # 가중치 0
        if nowHeight == nextHeight or nowHeight + 1 == nextHeight or nowHeight - 1 == nextHeight or min(nowHeight * 2, 20) == nextHeight:
            if dist[nowIdx] <= dist[nextIdx] and dist[nowIdx] < K:
                dist[nextIdx] = dist[nowIdx]
                d.appendleft([nextIdx, nextHeight])

        else:
            if dist[nowIdx] + 1 <= dist[nextIdx] and dist[nowIdx] + 1 < K:
                dist[nextIdx] = dist[nowIdx] + 1
                d.append([nextIdx, nextHeight])

print("-1" if dist[N] > K else dist[N])