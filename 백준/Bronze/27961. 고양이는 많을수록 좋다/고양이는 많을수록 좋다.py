n = int(input())
if n > 0:
    cat = 1
    count = 1
else:
    cat = 0
    count = 0
while True:
    if cat >= n:
        break
    cat *= 2
    count += 1

print(count)
