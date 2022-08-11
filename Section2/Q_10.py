# 점수계산

# 내 풀이
# n = int(input())
# arr = list(map(int, input().split()))
# count, score = 1, 0
#
# for x in arr:
#     if x == 1:
#         score += count
#         count += 1
#     else:
#         count = 1
# print(score)


# 강사 풀이
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
