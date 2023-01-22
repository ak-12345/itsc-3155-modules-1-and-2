list = []

for i in range(5):
    letter = str(input(f"Enter: {i+1}: "))
    list.append(letter)

words = ' '.join(list)

print("Letters: ", list)
print("String: ", words)