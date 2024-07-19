import entity

def update_location(entity, map):
    row_index = entity.row
    col_index = entity.col

    collision_check(entity, map)
    
    map[row_index][col_index] = entity

def remove_location(player, map):
    row_index = player.row
    col_index = player.col
    map[row_index][col_index] = entity.Empty(row_index,col_index, None, None)

def move_up(player, map):
    if player.row == 0: return
    remove_location(player, map)
    player.row -= 1
    update_location(player, map)

def move_down(player, map):
    if player.row == len(map) - 1: return
    remove_location(player, map)
    player.row += 1
    update_location(player, map)

def move_left(player, map):
    if player.col == 0: return
    remove_location(player, map)
    player.col -= 1
    update_location(player, map)

def move_right(player, map):
    if player.col == len(map[0]) - 1: return
    remove_location(player, map)
    player.col += 1
    update_location(player, map)

def yellow_flash(player, map):
    if player.has_flash:
        player.has_flash = False
        flash = player.flash
        player.flash = None

        remove_location(player, map)
        player.row = flash.row
        player.col = flash.col
        update_location(player, map)

        print("Whoosoosh")
    else:
        player.has_flash = True
        row = player.row
        col = player.col

        get_direction(player, map)
        player.flash = entity.innit_flash(row, col, map, None)
        print("Flash Marker Placed")

def get_direction(player, map):
    troll = 0
    while True:
        troll += 1
        try:
            direction = input("Enter direction: ")
            validate_input(direction)
            break
        except ValueError:
            print("Please enter a valid direction!")
    
    if direction == 'w':
        move_up(player, map)
    elif direction == 's':
        move_down(player, map)
    elif direction == 'a':
        move_left(player, map)
    elif direction == 'd':
        move_right(player, map)
    elif direction == 'f':
        yellow_flash(player, map)


def validate_input(user_input):
    valid_inputs = {'w', 'a', 's', 'd', 'f'}
    if user_input not in valid_inputs:
        raise ValueError("Invalid input. Please enter 'w', 'a', 's', or 'd'.")
    
def collision_check(object, map):
    if type(map[object.row][object.col]) != entity.Empty:
        object.on_collide(type(map[object.row][object.col]))