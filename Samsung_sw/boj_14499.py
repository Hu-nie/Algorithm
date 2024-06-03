def roll_dice(c, dice):
    # 동쪽
    if c == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서쪽
    elif c == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북쪽
    elif c == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 남쪽
    elif c == 4:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return dice

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for c in command:
    nx = x + dx[c-1]
    ny = y + dy[c-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    dice = roll_dice(c, dice)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
    x = nx
    y = ny
