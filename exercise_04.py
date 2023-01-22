#This is pythons scanner
n = int(input("Enter a number: "))
nums = []

#input float numbers with a range of n
for i in range(n):
    num = input(f"Enter a num {i+1}: ")
    nums.append(float(num))
#print list
print("Numbered list: " , nums)

#average
avg = sum(nums)/len(nums)

print("Average: ", avg)