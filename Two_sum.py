numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Indices:", i, j)