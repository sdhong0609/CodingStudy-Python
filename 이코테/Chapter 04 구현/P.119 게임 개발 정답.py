""" P.119 게임 개발 정답"""

# 가로 길이 n, 세로 길이 m 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * n for _ in range(m)]
# 현재 캐릭터의 좌표와 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 캐릭터 좌표를 방문으로 처리

# 전체 맵 정보 입력받기
array = [list(map(int, input().split())) for _ in range(m)]

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전 함수 (0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    # 이동할 좌표 설정
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후에 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 방문 이력 맵의 위치 값도 0, 전체 맵의 위치 값도 0
        d[nx][ny] = 1  # 해당 좌표 값을 방문으로 처리
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 (d 혹은 array의 해당 좌표 값이 1인 경우)
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 바라보는 방향을 유지한 채 한 칸 뒤로 좌표 설정
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0  # 뒤로 이동한 다음 다시 네 방향 체크를 해야 되니까 turn_time 값을 다시 0으로

print(count)  # 정답 출력
