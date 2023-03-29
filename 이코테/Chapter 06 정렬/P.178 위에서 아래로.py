""" P.178 위에서 아래로 """

""" 내 풀이 """
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
print(*data)
