arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
s = input()
for x in arr:
    if x in s:
        cnt += s.count(x)
        s = s.replace(x, ' ')

s = s.replace(' ', '')
print(cnt + len(s))
