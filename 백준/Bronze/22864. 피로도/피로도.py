a, b, c, m = map(int, input().split())
result = 0
tiredness = 0
time = 24

for _ in range(24):
    if tiredness + a > m:
        tiredness -= c
        if tiredness < 0:
            tiredness = 0
    else:
        tiredness += a
        result += b

print(result)