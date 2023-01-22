num = []
even = []

while True:
    u_input = input("Enter a num or 'QUIT': ")
    if u_input == "QUIT":
        break
    else:
        numbs = int(u_input)
        num.append(num)
        if numbs % 2 == 0:
            even.append(numbs) 

print("Numbers: ", num)
print("Even: ", even)