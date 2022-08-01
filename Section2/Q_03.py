# K번째 큰 수

# 내 풀이
# n, k = map(int, input().split())
#
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# print(arr)
# arr2 = []
# a, b, c = 0, 1, 2
#
# for x in range(a, len(arr)):
#     for y in range(b, len(arr)):
#         for z in range(c, len(arr)):
#             arr2.append(arr[x] + arr[y] + arr[z])
#         c += 1
#     b += 1
#
# arr2.sort(reverse=True)
# print(arr2[k - 1])


# 강사 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()  # 중복 제거 자료형
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])
res = list(res)
res.sort(reverse=True)
print(res[k - 1])
