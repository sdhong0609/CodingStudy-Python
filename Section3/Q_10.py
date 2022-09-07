# 스도쿠 검사

# 내 풀이
# a = [list(map(int, input().split())) for _ in range(9)]
# dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
# dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]
# isRight = True
#
# for i in range(9):
#     if len(set(a[i])) != 9:
#         isRight = False
#         break
#
# if isRight:
#     for i in range(9):
#         s = set()
#         for j in range(9):
#             s.add(a[j][i])
#         if len(s) != 9:
#             isRight = False
#             break
#
# if isRight:
#     for i in range(0, 9, 3):
#         s = set()
#         for j in range(0, 9, 3):
#             for k in range(9):
#                 s.add(a[i+dx[k]][j+dy[k]])
#             if len(s) != 9:
#                 isRight = False
#                 break
#
# if isRight:
#     print('YES')
# else:
#     print('NO')


# 강사 풀이
def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False

    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")