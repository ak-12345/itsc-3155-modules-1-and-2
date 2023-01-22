row = int(input("Enter a number from 1 to 5: "))
column = int(input("Enter a number from 1 to 5: "))

grid = [[0 for i in range(5)] for j in range(5)]

grid[row - 1][column - 1] = 1

for row in grid:
    print(row)