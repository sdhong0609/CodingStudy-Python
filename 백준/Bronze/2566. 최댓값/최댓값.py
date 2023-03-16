a = [list(map(int, input().split())) for _ in range(9)]
max_list = []
j_list = []
for x in a:
    j_list.append(x.index(max(x)))
    max_list.append(max(x))

m = max(max_list)
print(m)
print(max_list.index(m)+1, j_list[max_list.index(m)]+1)