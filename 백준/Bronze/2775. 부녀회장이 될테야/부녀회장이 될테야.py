t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    d = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        d[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i-1][j] + d[i][j-1]

    print(d[k][n])