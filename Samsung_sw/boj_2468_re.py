from collections import deque

def bfs(x, y, k):
    dx = [1, -1, 0, 0]  # 상하좌우 이동을 위한 방향 벡터
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 위치가 지도 범위 내에 있고, 안전 영역이며, 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < N and Maps[nx][ny] > k and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
    return count

# 입력 받기
N = int(input("N 값을 입력하세요: "))
Maps = [list(map(int, input().split())) for _ in range(N)]
height = max(map(max, Maps))  # 지도에서 가장 높은 높이

max_safe_areas = 0  # 안전 영역의 최대 개수

# 각 높이 k에 대해 안전 영역 찾기
for k in range(height + 1):
    visited = [[0] * N for _ in range(N)]  # 방문 여부를 저장할 배열
    safe_areas_count = 0  # 현재 높이 k에서의 안전 영역 개수
    for x in range(N):
        for y in range(N):
            # 현재 위치가 안전 영역이며 방문하지 않은 경우
            if Maps[x][y] > k and visited[x][y] == 0:
                bfs(x, y, k)
                safe_areas_count += 1
    max_safe_areas = max(max_safe_areas, safe_areas_count)

print("최대 안전 영역 개수:", max_safe_areas)
