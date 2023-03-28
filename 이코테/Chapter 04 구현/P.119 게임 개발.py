""" P.119 게임 개발 """

""" 내 풀이 """
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1
field = [list(map(int, input().split())) for _ in range(n)]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or ny < 0 or nx > m or ny > n or d[nx][ny] == 1 or field[nx][ny] == 1:
        turn_time += 1
    else:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if field[nx][ny] == 0:
            x, y = nx, ny
        turn_time = 0
        if field[nx][ny] == 1:
            break

print(count)
