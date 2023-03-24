t = int(input())
for _ in range(t):
    money = int(input())
    quarter = money // 25
    money -= 25 * quarter
    dime = money // 10
    money -= 10 * dime
    nickel = money // 5
    money -= 5 * nickel
    penny = money
    print(quarter, dime, nickel, penny)
