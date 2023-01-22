num = []
one =[]

for i in range(10):
    numbs = int(input(f"Enter num {i+1}: "))
    num.append(numbs)

for numbs in num:
    if num.count(numbs) == 1:
        one.append(numbs)

print("List: ", num)
print("List2: : ", one)