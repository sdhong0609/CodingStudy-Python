# 점수계산

# 내 풀이
n = int(input())
a = list(map(int, input().split()))
score = 0
res = 0

for x in a:
    if x == 1:
        score += 1
        res += score
    else:
        score = 0
print(res)


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
