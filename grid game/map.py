import constants
import entity

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def create_map(rows, cols):
    map = []
    for i in range(rows):
        row = []
        for j in range(cols):
            new_entity = entity.Empty(i,j,None,None)
            row.append(new_entity)
        map.append(row)
    return map

def print_map(map, rows, cols):
    # printing x
    print(YELLOW + "  ", end='')

    print("\033[4m", end='')
    for i in range(0, rows):
        print(i, end='')

    print(RESET, end='')

    print()
    
    #printing y
    for i in range(rows):
        print(YELLOW, end='')
        print(i, end='|')
        print(RESET, end='')
        for j in range(cols):
            #add colour code
            if type(map[i][j]) == entity.Player:
                print(GREEN, end='')
            elif type(map[i][j]) == entity.Enemy:
                print(RED, end='')
            elif type(map[i][j]) == entity.Sword:
                print(BLUE, end='')
            elif type(map[i][j]) == entity.Flash:
                print(YELLOW, end='')

            print(map[i][j].display(), end='')
            print(RESET, end='')
        print()

def get_map_dimensions():
    while True:
        try:
            rows = int(input("Enter rows: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            cols = int(input("Enter columns: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    
    return rows, cols