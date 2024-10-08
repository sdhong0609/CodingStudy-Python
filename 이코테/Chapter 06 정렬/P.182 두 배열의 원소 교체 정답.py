""" P.182 두 배열의 원소 교체 정답 """

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # a의 원소가 b의 원소보다 크거나 같을 때, 반복문 탈출
    # 꼭 k번 반복해야 한다는 것이 아니라 최대 k번 반복할 수 있다는 것이므로
    # k번보다 더 적게 반복 가능, 그래서 반복문 탈출이 필요
    else:
        break

print(sum(a))
