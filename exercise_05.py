list1 = []
for i in range(5):
    list1.append(int(input("Enter number for list : ")))

list2 = []
for i in range(5):
    list2.append(int(input("Enter number for list : ")))

leftOv = []
for i in list1:
    if i in list2 and i not in leftOv:
        leftOv.append(i)

print("List 1: ", list1)
print("List 2: ", list2)
print("LeftOver: ", leftOv)