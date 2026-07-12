numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort()

second_largest = numbers[-2]
print("Second Largest: ", second_largest)
