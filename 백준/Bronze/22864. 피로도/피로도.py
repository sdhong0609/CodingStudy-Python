a, b, c, m = map(int, input().split())
result = 0
tiredness = 0
time = 24

while True:
    if tiredness + a > m:
        tiredness -= c
        if tiredness < 0:
            tiredness = 0
    else:
        tiredness += a
        result += b
    time -= 1
    if time == 0:
        break

print(result)