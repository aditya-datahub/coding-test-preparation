numbers = list(map(int, input("Enter numbers: ").split()))

print("Original List: ", numbers)

numbers = list(sorted(set(numbers)))

print("Unique Numbers: ", numbers)
