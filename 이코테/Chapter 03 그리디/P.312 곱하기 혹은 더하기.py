""" P.312 곱하기 혹은 더하기 """

""" 내 풀이 """

s = list(map(int, input()))
print(s)

# 무조건 곱하기를 우선시 해야한다. 0이 있을 때만 더하기를 해야 한다
result = s[0]
for i in range(1, len(s)):
    if s[i-1] == 0:
        result += s[i]
    else:
        result *= s[i]

print(result)

# 입력 1
# 02984
# 출력 1
# 576

# 입력 2
# 567
# 출력 2
# 210
