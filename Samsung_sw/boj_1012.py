from collections import deque
def bfs(x, y, board):
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append([x, y])
    board[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                q.append((nx,ny))
                board[nx][ny] = 0

    return cnt



T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())

    board = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1

    res = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = bfs(i, j, board)

                res += 1

    print(res)