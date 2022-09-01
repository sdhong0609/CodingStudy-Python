# 카드 역배치(정올 기출)

# 내 풀이
# arr = [0]*21
# for i in range(1, 21):
#     arr[i] = i
#
# for i in range(10):
#     a, b = map(int, input().split())
#     sum = a+b
#     for j in range(a, sum//2+1):
#         tmp = arr[j]
#         arr[j] = arr[sum-j]
#         arr[sum-j] = tmp
#
# for i in range(1, 21):
#     print(arr[i], end=' ')


# 강사 풀이
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
