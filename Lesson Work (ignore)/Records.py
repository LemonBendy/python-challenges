#array = ['','','','','','']
#for i in range(0, 6):
#    array[i] = i

#print(array)

#for j in range(len(array)-1, -1, -1):
#    print(array[j])

# name = ['','','','','','']
# for i in range(0, 6):
#     name[i] = input("Enter name: ")

# #search for name
# search = input("Enter name to search: ")
# for i in range(0, 6):
#     if search == name[i]:
#         print(f"Name found at position {i+1}"})
#         break
#     elif i == 5:
#         print("Name not found")

# outlet1sales = [10, 12, 15, 10]
# outlet2sales = [5,8,3,6]
# outlet3sales = [10,12,15,10]
# total = [0,0,0,0]
# for quarter in range(0, 4):
#     total[quarter] = outlet1sales[quarter] + outlet2sales[quarter] + outlet3sales[quarter]
#     print(f"total sales for quarter {quarter+1} is {total[quarter]}")

# grid = [["O","x","x","x"],
#         ["x","x","x","x"],
#         ["x","x","x","x"],
#         ["x","x","x","x"],
#         ["x","x","x","x"],
#         ["x","x","x","x"]]

# for row in range(0, 6):
#     for column in range(0, 4):
#         print(grid[row][column], end="")
#     print()

# positionx, positiony= input("Enter position: ").split(",")
# positionx = int(positionx) - 1
# positiony = int(positiony) - 1

# for i in range(0, 6):
#     for j in range(0, 4):
#         if grid[i][j] == "O":
#             grid[i][j] = "x"
#             break

# grid[positionx][positiony] = "O"

# for row in range(0, 6):
#     for column in range(0, 4):
#         print(grid[row][column], end="")
#     print()


grid = [["" for _ in range(10)] for _ in range(6)]

for row in range(0, 6):
    for column in range(0, 9):
        grid[row][column] = "empty, "

def print_grid():
    for row in range(0, 6):
        for column in range(0, 9):
            print(grid[row][column], end="")
        print()

def add_car_to_space(row, column, reg):
    if grid[row][column] == "empty, ":
        grid[row][column] = reg + ", "
        return True
    else:
        return False
    
def remove_car_from_space(row, column):
    if grid[row][column] != "empty, ":
        grid[row][column] = "empty, "
        return True
    else:
        return False
    
def find_car(reg):
    for row in range(0, 6):
        for column in range(0, 9):
            if grid[row][column] == reg:
                return row, column
    return -1, -1

if __name__ == '__main__':
    add_car_to_space(0, 0, "AB12CDE")
    add_car_to_space(0, 1, "AB12CDF")
    add_car_to_space(0, 2, "AB12CDG")
    add_car_to_space(0, 3, "AB12CDH")
    print_grid()

    

