numbers = list(map(int, input("Enter numbers: ").split()))
start=0
end=len(numbers)-1

while start<end:
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start+=1
    end-=1

print("Reversed list: ", numbers)