numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter the number to find: "))

for index, value in enumerate(numbers):
    if value == n:
        print(n, "found at index", index)
        break
else:
    print(n, "not found") 