import random

def random_number():
    numbers = []
    for index in range(10):
        number = random.randint(1 , 50)
        numbers.append(number)
    return numbers

print(random_number())
