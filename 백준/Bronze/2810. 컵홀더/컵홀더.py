n = int(input())
seat = input()
count_ll = seat.count('LL')
count_holder = n + 1 - count_ll
if count_holder < n:
    print(count_holder)
else:
    print(n)
