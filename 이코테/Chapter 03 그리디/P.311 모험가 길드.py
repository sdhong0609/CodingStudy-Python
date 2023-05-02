""" P.311 모험가 길드 """

""" 내 풀이 """

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 여행을 떠날 수 있는 그룹 수의 최댓값

n = int(input())
gongPoDo = list(map(int, input().split()))
count = 0

gongPoDo.sort()  # 오름차순 정렬 (큰 수가 뒤로)
print(gongPoDo)

# 최댓값을 구하고 공포도가 높은 인원을 그 그룹에 배치해야 한다
while True:
    for _ in range(max(gongPoDo)):
        gongPoDo.pop()
    count += 1
    if len(gongPoDo) <= 0:
        break

print(count)

# 입력
# 5
# 2 3 1 2 2

# 출력
# 2
