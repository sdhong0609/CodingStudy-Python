""" P.201 떡볶이 떡 만들기 """

""" 내 풀이 """
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
cut = [0] * n


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        for i in range(n):
            cut[i] = array[i] - mid
            if cut[i] < 0:
                cut[i] = 0

        if sum(cut) == target:
            return mid
        elif sum(cut) < target:
            end = mid - 1
        else:
            start = mid + 1
    return None


result = binary_search(data, m, 0, max(data))
print(result)
