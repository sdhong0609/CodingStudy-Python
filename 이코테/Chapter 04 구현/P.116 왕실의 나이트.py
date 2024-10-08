""" P.116 왕실의 나이트 """

""" 내 풀이 """
# dx = [-2, -1, 1, 2, 2, 1, -1, -2]
# dy = [-1, -2, -2, -1, 1, 2, 2, 1]
# spot = list(input())
# x = ord(spot[0]) - ord('a') + 1
# y = int(spot[1])
# cnt = 0
#
# for i in range(len(dx)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     cnt += 1
#
# print(cnt)

""" 내 풀이 2 """

# 체스판 2차원 리스트로 생성
d = [[0] * 8 for _ in range(8)]
# 입력값 중 알파벳을 인덱스로 바꾸기 위한 리스트
column_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 체스판 이동을 위한 리스트
dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]

# 데이터 입력
data = input()
column = data[0]
row = data[1]

# 각각의 index 값 구하기
column_index = column_list.index(column)
row_index = int(row) - 1

count = 0
for i in range(8):
    x = row_index + dx[i]
    y = column_index + dy[i]
    if x < 0 or y < 0 or x >= 8 or y >= 8:  # 이동한 좌표가 체스판을 벗어나면 continue
        continue
    else:
        count += 1

print(count)
