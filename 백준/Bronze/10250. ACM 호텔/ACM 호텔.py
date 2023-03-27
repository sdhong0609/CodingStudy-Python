t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        h_string = str(h)
        w_string = str(n//h)
    else:
        h_string = str(n % h)
        w_string = str(n // h + 1)
    if int(w_string) < 10:
        print(h_string + '0' + w_string)
    else:
        print(h_string + w_string)
