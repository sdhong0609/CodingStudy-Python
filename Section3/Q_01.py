# 회문 문자열 검사

# 내 풀이
# n = int(input())
# cnt = 0
# for i in range(n):
#     string = input()
#     reversed_string = string[::-1]
#     cnt += 1
#     if string.lower() == reversed_string.lower():
#         print("#" + str(cnt), "YES")
#     else:
#         print("#" + str(cnt), "NO")


# 강사 풀이 (권장)
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))


# 강사 풀이 2
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d YES" % (i+1))
#     else:
#         print("#%d NO" % (i+1))
