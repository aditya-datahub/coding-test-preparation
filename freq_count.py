s = input("enter a sentence: ")
s = s.replace(" ", "")   # spaces hata do

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in freq:
    print(f"{char}:{freq[char]} ", end=" ")
