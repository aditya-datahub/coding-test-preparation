numbers=list(map(int, input("Enter numbers:").split()))

freq={}
for num in numbers:
    freq[num] = freq.get(num, 0)+1

for num in freq:
    print(f"{num}:{freq[num]}", end=" ")