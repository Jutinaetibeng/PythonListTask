numbers = [ 8, 3, 7, 2, 9, 12,14]

total = 0
for index in range(0, len(numbers), 2):
    total += numbers[index]

print(total)
