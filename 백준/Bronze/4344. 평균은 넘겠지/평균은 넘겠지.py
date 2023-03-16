c = int(input())

for _ in range(c):
    a = list(map(int, input().split()))
    ave = sum(a[1:])/len(a[1:])
    cnt = 0
    for i in range(1, len(a)):
        if a[i] > ave:
            cnt += 1
    percent = cnt / len(a[1:]) * 100
    print(format(percent, ".3f") + "%")