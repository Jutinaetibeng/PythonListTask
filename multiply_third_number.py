numbers = input("Enter numbers: ")
numbers = numbers.split()
total = 0
largest = int(numbers[0])
smallest = int(numbers[0])
product = 1
for index in range(len(numbers)):
   number = int(numbers[index])
   total = total + number
    
   if number > largest:
       largest = number

   if number < smallest:
       smallest = number

   if index % 3 == 2:
       product =  product * number
average = total / len(numbers)

print("Average = ", average)
print("Largest = ", largest)
print("Smallest = ", smallest)
print("Product of third positions = ", product)

