input_data = input()

start = 0
end = 10

while True:
    print(input_data[start:end])
    if end == len(input_data):
        break
    start += 10
    end += 10
    if end > len(input_data):
        end = len(input_data)
