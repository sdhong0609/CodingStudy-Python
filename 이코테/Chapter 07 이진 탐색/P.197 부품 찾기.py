""" P.197 부품 찾기 """

""" 내 풀이 """
import sys

input = sys.stdin.readline
n = int(input())
store = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

store.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for x in request:
    result = binary_search(store, x, 0, n-1)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
