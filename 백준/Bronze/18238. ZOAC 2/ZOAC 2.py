def go_time(A, B):
    T1 = abs(ord(B) - ord(A))
    return min(T1, 26 - T1)


S = "A" + input()
time = 0
for i in range(len(S) - 1):
    time += go_time(S[i], S[i + 1])
print(time)
