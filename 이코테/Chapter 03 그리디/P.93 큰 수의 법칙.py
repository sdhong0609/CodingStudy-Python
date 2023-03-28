""" P.93 큰 수의 법칙 """

""" 내 풀이 1 """
# import sys
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
# arr = sorted(arr, reverse=True)
# sum = 0
# for i in range(m):  # 1,2,3,4,.....m
#     if i > k and i % k == 1:
#         sum += arr[1]
#         continue
#     sum += arr[0]
# print(sum)


""" 내 풀이 2 """
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

first = array[0]
second = array[1]

result = (first * (k + 1) - (first - second)) * (m // (k + 1))

for i in range(m % (k + 1)):
    result += first

print(result)
