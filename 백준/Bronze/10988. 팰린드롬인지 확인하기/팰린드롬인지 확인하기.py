s = input()
res = 1
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        res = 0
        break
print(res)