""" P.100 1이 될 때까지 정답 """

n, k = map(int, input().split())
count = 0

while True:
    # 나누어 떨어지는 수를 먼저 계산해서 target에 넣는다
    target = (n // k) * k
    # 나누어 떨어지는 수가 될 때까지 -1을 해야 하는 횟수를 count에
    count += (n - target)
    n = target
    # n보다 k가 더 크면 나눌 수 없으므로 break
    if n < k:
        break
    # k로 나누기
    n = n // k
    count += 1

# 마지막으로 남은 수에 대하여 1씩 빼는 횟수를 더하기 (n이 0이면 -1을 더해서 횟수를 줄임)
count += (n - 1)

print(count)
