import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
MAX = arr[0]
answer = []
cnt = 0

for i in range(1, n):
    if MAX > arr[i]:
        cnt += 1
    else:
        MAX = arr[i]
        answer.append(cnt)
        cnt = 0

# 예를 들어, 6 4 10 2 5 7 11 1 2 3 4 처럼 마지막 cnt값이 최댓값이 되는 경우를 위해 cnt를 append해야 함
# answer가 비어있어도 cnt값 0을 append를 하기 때문에 에러 발생하지 않는다. 이러한 경우 최댓값은 0
answer.append(cnt)
print(max(answer))
