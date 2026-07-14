n = int(input("Enter N: "))
numbers = list(map(int, input("Enter numbers: ").split()))

expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing Number:", expected - actual)