def bfs(x, y):
    from collections import deque

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M and Maps[nx][ny] == 1:
                q.append((nx, ny))
                Maps[nx][ny] =  Maps[x][y] + 1

    return Maps[N-1][M-1]


N, M = map(int, input().split())
Maps = [list(map(int, input())) for _ in range(N)]

dx = [1,-1, 0, 0]
dy = [0, 0,-1, 1]



print(bfs(0,0))
