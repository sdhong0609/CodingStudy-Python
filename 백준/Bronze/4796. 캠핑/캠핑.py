i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    cycle = (v // p) * l
    rest = v % p
    if rest > l:
        rest = l
    print(f"Case {i}: {cycle + rest}")
    i += 1