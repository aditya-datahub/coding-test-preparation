numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to find: "))

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index:", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")