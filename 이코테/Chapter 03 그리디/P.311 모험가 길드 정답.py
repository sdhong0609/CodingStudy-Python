""" P.311 모험가 길드 정답 """

n = int(input())
data = list(map(int, input().split()))  # 공포도 리스트
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for x in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= x:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력

# 입력 1
# 5
# 2 3 1 2 2
# 출력 1
# 2

# 입력 2
# 7
# 1 2 3 1 2 2 1
# 출력 2
# 4

# 입력 3
# 15
# 1 2 3 4 5 1 2 3 4 5 1 1 1 1 1
# 출력 3
# 9
