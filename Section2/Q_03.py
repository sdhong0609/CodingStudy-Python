# K번째 큰 수

# 내 풀이
n, k = map(int, input().split())
arr = list(map(int, input().split()))
a = set()
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for l in range(j+1, n):
            sum = arr[i] + arr[j] + arr[l]
            a.add(sum)
a = list(a)
a.sort(reverse=True)
print(a[k-1])


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
