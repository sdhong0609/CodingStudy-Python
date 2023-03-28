def replace_five_to_six(x):
    return str(x).replace('5', '6')


def replace_six_to_five(x):
    return str(x).replace('6', '5')


a, b = input().split()

a = replace_six_to_five(a)
b = replace_six_to_five(b)
min_value = int(a) + int(b)

a = replace_five_to_six(a)
b = replace_five_to_six(b)
max_value = int(a) + int(b)

print(min_value, max_value)
