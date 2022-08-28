# 점수계산

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
