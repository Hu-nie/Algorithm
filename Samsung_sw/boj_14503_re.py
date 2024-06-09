from collections import deque

def bfs(x, y, d):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((x, y))
    maps[x][y] = 2  # 시작 위치를 청소했다고 표시
    cnt = 1

    while q:
        x, y = q.popleft()
        flag = False

        for _ in range(4):
            d = (d + 3) % 4  # 왼쪽으로 회전
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                q.append((nx, ny))
                maps[nx][ny] = 2
                cnt += 1
                flag = True
                break

        if not flag:  # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
            bx = x - dx[d]
            by = y - dy[d]
            if 0 <= bx < N and 0 <= by < M and maps[bx][by] != 1:  # 뒤로 이동
                q.append((bx, by))
            else:
                print(cnt)
                return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

bfs(r, c, d)
