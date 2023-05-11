import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

i = 0
count = 0
while True:
    if i >= n:
        break
    if array[i] != i+1:
        array.pop(i)
        count += 1
        n -= 1
        i -= 1
    i += 1

print(count)
