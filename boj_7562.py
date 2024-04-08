from collections import deque


def bfs(matrix, now, goal, visited, i):

    
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append(now)
    visited[now[0]][now[1]] =True

    while q:
        x, y = q.popleft()
        if x == goal[0] and y == goal[1]:
            return 0
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx>= n  or ny < 0 or ny>= n :
                    continue
                if nx == goal[0] and ny == goal[1]:
                    visited[nx][ny] = True
                    print(matrix)
                    return matrix[x][y]+1
                
                if visited[nx][ny] == False:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    matrix[nx][ny] = matrix[x][y] +1 


for _ in range(int(input())):
    n = int(input())
    now = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    
    matrix = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    print(bfs(matrix, now, goal, visited, n))

