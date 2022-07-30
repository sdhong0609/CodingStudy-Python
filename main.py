# n = int(input())
# for i in range(1, n + 1):
#     print(i)

# n = int(input())
# for i in range(1, n + 1):
#     if i % 2 == 1:
#         print(i)

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
#
# print(sum)

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
