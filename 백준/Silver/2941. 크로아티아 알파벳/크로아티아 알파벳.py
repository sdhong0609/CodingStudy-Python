arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for x in arr:
    if x in s:
        s = s.replace(x, 'a')

print(len(s))
