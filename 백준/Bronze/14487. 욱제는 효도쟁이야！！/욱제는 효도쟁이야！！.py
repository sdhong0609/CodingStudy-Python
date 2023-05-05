n = int(input())
costs = list(map(int, input().split()))

print(sum(costs) - max(costs))

# 입력 1
# 5
# 1 6 5 2 4
# 출력 1
# 12

# 입력 2
# 4
# 100 100 100 101
# 출력 2
# 300
