# 두 리스트 합치기

# 내 풀이
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# c = list()
#
# p1, p2 = 0, 0
#
# while p1 < n and p2 < m:
#     if a[p1] <= b[p2]:
#         c.append(a[p1])
#         p1 += 1
#     else:
#         c.append(b[p2])
#         p2 += 1
#
# if p1 == n:
#     list = c + b[p2:m]
# else:
#     list = c + a[p1:n]
#
# for x in list:
#     print(x, end=' ')


# 강사 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
for x in c:
    print(x, end=' ')
