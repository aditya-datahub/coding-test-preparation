numbers = list( map( int, input("Enter numbers: ").split() ) )

even_count = odd_count = 0

for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Total even Numbers: ", even_count)
print("Total odd Numbers: ", odd_count)
