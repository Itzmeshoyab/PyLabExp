import random
numbers = []
for i in range(20):
    num = random.randint(1, 100)
    numbers.append(num)
print("List of numbers:")
for i in range(20):
    print(numbers[i], end=" ")
print("\n")
total = 0
for i in range(20):
    total = total + numbers[i]
average = total / 20
print("Average:", average)
