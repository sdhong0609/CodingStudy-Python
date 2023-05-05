n, m = map(int, input().split())
present = 0
target = m - 1
cards = []
for _ in range(m):
    win, lose = map(int, input().split())
    if win >= n:
        present += 1
    else:
        cards.append((win, lose))

result = 0
diff = []
if present >= target:
    print(0)
else:
    target -= present
    for card in cards:
        diff.append(n - card[0])
    diff.sort()
    result += sum(diff[:target])
    print(result)
