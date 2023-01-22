#pythons input
use = input("Enter: ")

char = list(use)

listSize = 3

list1 = [char[i:i + listSize] for i in range(0, len(char), listSize)]

print(list1)