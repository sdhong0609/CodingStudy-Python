# 봉우리

# 내 풀이
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# a.insert(0, [0]*(n+2))
# a.append([0]*(n+2))
# for i in range(1, n+1):
#     a[i].insert(0, 0)
#     a[i].append(0)
#
# cnt = 0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if a[i][j] <= a[i-1][j]:
#             continue
#         elif a[i][j] <= a[i][j-1]:
#             continue
#         elif a[i][j] <= a[i][j+1]:
#             continue
#         elif a[i][j] <= a[i+1][j]:
#             continue
#         else:
#             cnt += 1
#
# print(cnt)


# 강사 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
