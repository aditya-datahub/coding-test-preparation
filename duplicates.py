numbers = list(map(int, input("Enter numbers: ").split()))

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1

duplicates = []
for num in freq:
    if freq[num] > 1:
        duplicates.append(num)

print("Duplicates:", duplicates)