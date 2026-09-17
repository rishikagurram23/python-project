string = input("Enter a word: ")
count = 0
for ch in string:
    count += 1
reverse = ""
i = count - 1
while i >= 0:
    reverse += string[i]
    i -= 1
print("Reversed word:", reverse)