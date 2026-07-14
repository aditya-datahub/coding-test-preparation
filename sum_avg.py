numbers = list(map(int, input("Enter numbers: ").split()))

sum = 0

for num in numbers:
    sum+=num

avg = sum/len(numbers)

print(sum)
print(avg)
