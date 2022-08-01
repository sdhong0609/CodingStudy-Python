# K번째 수

# 내 풀이
# t = int(input())
# answer = []
# for i in range(t):
#     n, s, e, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr2 = arr[s - 1:e]
#     arr2.sort()
#     answer.append(arr2[k-1])
#
# for i in range(t):
#     print("#{}".format(i+1), answer[i])


# 강사 풀이
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" % (t+1, a[k-1]))
