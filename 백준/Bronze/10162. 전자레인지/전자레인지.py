t = int(input())  # 초(second)로 입력
# A: 300초, B: 60초, C: 10초

if t % 10 != 0:
    print(-1)
else:
    a = t//300
    t %= 300
    b = t//60
    t %= 60
    c = t//10
    print(a, b, c)