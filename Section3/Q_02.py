# 숫자만 추출

# 내 풀이
# s = input()
# res = ''
# for i in range(len(s)):
#     if (s[i] == '0' and res != '') or '0' < s[i] <= '9':
#         res += s[i]
# print(res)
#
# res = int(res)
# cnt = 0
# for i in range(1, int(res**(1/2)) + 1):
#     if res % i == 0:
#         cnt += 1
# print(cnt*2)


# 강사 풀이
s = input()
res = 0
for x in s:
    if x.isdecimal():
       res = res*10 + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
