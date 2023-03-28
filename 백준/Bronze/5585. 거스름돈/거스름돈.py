coin_types = [500, 100, 50, 10, 5, 1]
n = int(input())
count = 0
charge = 1000 - n

for coin in coin_types:
    count += charge // coin
    charge %= coin

print(count)