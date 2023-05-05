def calculate_diff(a, b):
    diff1 = ord(a) - ord(b)
    if diff1 < 0:
        diff1 += 26
    diff2 = ord(b) - ord(a)
    if diff2 < 0:
        diff2 += 26

    if diff1 < diff2:
        return diff1
    else:
        return diff2


s = input()
result = calculate_diff('A', s[0])

for i in range(len(s) - 1):
    result += calculate_diff(s[i], s[i + 1])

print(result)
