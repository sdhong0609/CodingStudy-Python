# K번째 수

t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = arr[s-1:e]
    arr2.sort()
    print("#"+str(i+1), arr2[k-1])
