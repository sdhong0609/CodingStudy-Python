""" P.312 곱하기 혹은 더하기 정답 """

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num


# 입력 1
# 02984
# 출력 1
# 576

# 입력 2
# 567
# 출력 2
# 210
