# """ 풀이 1"""
# while True:
#     try:
#         a, b, c = map(int, input().split())
#         count = 0
#         while True:
#             if a + 2 == b + 1 == c:
#                 break
# 
#             if c - b > b - a:
#                 a, b, c = b, b + 1, c
#                 count += 1
#             else:
#                 a, b, c = a, b - 1, b
#                 count += 1
# 
#         print(count)
#     except EOFError:
#         break

""" 풀이 2"""
while True:
    try:
        a, b, c = map(int, input().split())
        print(max(b - a, c - b) - 1)
    except EOFError:
        break

# 입력 1
# 2 3 5
# 3 5 9
# 출력 1
# 1
# 3
