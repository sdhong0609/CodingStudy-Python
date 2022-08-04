# 대표값

# 내 풀이
# n = int(input())
# arr = list(map(int, input().split()))
#
# sum = 0
# for i in arr:
#     sum += i
# average = round(sum/n)
#
# arr2 = []
# for i in range(n):
#     arr2.append(abs(arr[i]-average))
#
# arr3 = []
# arr4 = []
# for i in range(n):
#     if arr2[i] == min(arr2):
#         arr3.append(i)
#         arr4.append(arr[i])
#
# arr5 = []
# for i in arr3:
#     if arr[i] == max(arr4):
#         arr5.append(i)
#
# print(average, arr5[0]+1)


# 강사 풀이
n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a) / n + 0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
