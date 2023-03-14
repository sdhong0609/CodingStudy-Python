Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
sum = 0
for x in a:
    for y in Number:
        if x in y:
            sum += Number.index(y) + 3
print(sum)