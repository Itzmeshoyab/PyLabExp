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
largest = numbers[0]
smallest = numbers[0]
for i in range(1, 20):
    if numbers[i] > largest:
        largest = numbers[i]
    if numbers[i] < smallest:
        smallest = numbers[i]
print("Largest value:", largest)
print("Smallest value:", smallest)
second_largest = -1
second_smallest = 101
for i in range(20):
    if numbers[i] > second_largest and numbers[i] != largest:
        second_largest = numbers[i]
    if numbers[i] < second_smallest and numbers[i] != smallest:
        second_smallest = numbers[i]
print("Second Largest value:", second_largest)
print("Second Smallest value:", second_smallest)
even_count = 0
for i in range(20):
    if numbers[i] % 2 == 0:
        even_count = even_count + 1
print("Number of even numbers:", even_count)
