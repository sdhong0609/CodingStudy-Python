# 소수(에라토스테네스 체)

n = int(input())
ch = [0]*(n+1)
cnt = 0
a = int(n**(1/2)+1) # 4 < 루트20 < 5

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
