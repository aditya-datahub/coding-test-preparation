numbers = list(map(int, input("Enter numbers: ").split()))

largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)