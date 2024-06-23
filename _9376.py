# https://www.acmicpc.net/problem/9376
# 참고: https://everenew.tistory.com/161
#      https://astrid-dm.tistory.com/418

from collections import deque
import sys
input = sys.stdin.readline

INF = 101 * 101 + 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    # 죄수들의 좌표
    prisonerCor = []
    Y, X = map(int, input().split())

    # 출구 좌표
    isDoor = [[False] * (X + 2) for _ in range(Y + 2)]

    # 0 : 빈공간(.), 죄수($)
    # 1 : 문 (#)
    # -1: 벽 (*)
    graph = [[-1] * (X + 2) for _ in range(Y + 2)]

    # dist1: 죄수1에서 bfs 수행
    dist1 = [[INF] * (X + 2) for _ in range(Y + 2)]
    # dist2 = 죄수2에서 bfs 수행
    dist2 = [[INF] * (X + 2) for _ in range(Y + 2)]
    # dist3 = 바깥에서 bfs 수행
    dist3 = [[INF] * (X + 2) for _ in range(Y + 2)]

    # 감옥의 바깥부분은 모두 거리비용 0으로 초기화
    for x in range(X + 2):
        graph[0][x] = graph[Y + 1][x] = 0
    for y in range(Y + 2):
        graph[y][0] = graph[y][X + 1] = 0

    # 평면도 입력
    for y in range(1, Y + 1):
        l = input()
        for x in range(1, X + 1):
            c = l[x - 1]
            if c == "$":
                prisonerCor.append([x, y])
                graph[y][x] = 0

            elif c == ".":
                graph[y][x] = 0

            elif c == "#":
                isDoor[y][x] = True
                graph[y][x] = 1

            elif c == "*":
                graph[y][x] = -1


    # 두 죄수들의 좌표 (x1, y1), (x2, y2)
    x1, y1 = prisonerCor[0]
    x2, y2 = prisonerCor[1]

    d = deque()

    # dist1: 죄수1에서 bfs 수행
    dist1[y1][x1] = 0
    d.append([x1, y1])
    while d:
        nowX, nowY = d.popleft()

        for i in range(4):
            nextX, nextY = nowX + dx[i], nowY + dy[i]

            if 0 <= nextX < (X + 2) and 0 <= nextY < (Y + 2):
                # 벽이면은 건너뛰기
                if graph[nextY][nextX] == -1:
                    continue

                if dist1[nextY][nextX] > dist1[nowY][nowX] + graph[nextY][nextX]:
                    dist1[nextY][nextX] = dist1[nowY][nowX] + graph[nextY][nextX]
                    if graph[nextY][nextX] == 0:
                        d.appendleft([nextX, nextY])
                    else:
                        d.append([nextX, nextY])

    # dist2: 죄수1에서 bfs 수행
    dist2[y2][x2] = 0
    d.append([x2, y2])
    while d:
        nowX, nowY = d.popleft()

        for i in range(4):
            nextX, nextY = nowX + dx[i], nowY + dy[i]

            if 0 <= nextX < (X + 2) and 0 <= nextY < (Y + 2):
                # 벽이면은 건너뛰기
                if graph[nextY][nextX] == -1:
                    continue

                if dist2[nextY][nextX] > dist2[nowY][nowX] + graph[nextY][nextX]:
                    dist2[nextY][nextX] = dist2[nowY][nowX] + graph[nextY][nextX]
                    if graph[nextY][nextX] == 0:
                        d.appendleft([nextX, nextY])
                    else:
                        d.append([nextX, nextY])

    # dist3: 감옥 바깥에서 bfs 수행
    dist3[0][0] = 0
    d.append([0, 0])
    while d:
        nowX, nowY = d.popleft()

        for i in range(4):
            nextX, nextY = nowX + dx[i], nowY + dy[i]

            if 0 <= nextX < (X + 2) and 0 <= nextY < (Y + 2):
                # 벽이면은 건너뛰기
                if graph[nextY][nextX] == -1:
                    continue

                if dist3[nextY][nextX] > dist3[nowY][nowX] + graph[nextY][nextX]:
                    dist3[nextY][nextX] = dist3[nowY][nowX] + graph[nextY][nextX]
                    if graph[nextY][nextX] == 0:
                        d.appendleft([nextX, nextY])
                    else:
                        d.append([nextX, nextY])

    sum = [[0] * (X + 2) for _ in range(Y + 2)]
    # 세 개의 dist값 더하기
    for y in range(Y + 2):
        for x in range(X + 2):
            sum[y][x] = dist1[y][x] + dist2[y][x] + dist3[y][x]

            if isDoor[y][x]:
                sum[y][x] -= 2

    # 죄수1, 죄수2, 상근이(제3자)가 어느 공통의 문에서 집결할 경우
    # 탈옥을 했다고 볼 수 있음.
    ans = INF
    for y in range(Y+2):
        for x in range(X+2):
            ans = min(ans, sum[y][x])

    print(ans)