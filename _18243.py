# 18243

import sys
input = sys.stdin.readline

INF = int(1e9) # 무한대 값

# N: 사람의 수
# K: 친구 관계의 수
N, K = map(int, input().split())

distance = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    A, B = map(int, input().split())
    distance[A][B] = distance[B][A] = 1

for i in range(1, N + 1):
    distance[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


isSmall = True

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] > 6:
            isSmall = False
            break

print("Small World!" if isSmall else "Big World!")