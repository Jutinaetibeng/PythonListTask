numbers = input("Enter numbers: ")
numbers = numbers.split()

total = 0
for index in range(len(numbers)):
    total = total + int(numbers[index])
average = total / len(numbers)
print(average)
