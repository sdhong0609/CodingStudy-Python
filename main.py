arr = [5, 3, 7, 9, 2, 5, 2, 6]

# arrMin = float('inf')  # python 에서 가장 큰 값 (무한대)
arrMin = arr[0]
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

arrMin = float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)
