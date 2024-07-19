import map
import entity
import move

if __name__ == "__main__":
    rows, cols = map.get_map_dimensions()

    game_map = map.create_map(rows,cols)

    entities = []

    player_1 = entity.innit_player(rows, cols, game_map, entities)
    entities.append(player_1)

    enemy = entity.innit_enemy(rows, cols, game_map, entities)
    entities.append(enemy)

    sword = entity.innit_sword(rows, cols, game_map, entities)
    entities.append(sword)
    
    map.print_map(game_map,rows,cols)
    while True:
        print("")

        move.get_direction(player_1, game_map)
        for object in entities:
            object.tick()

        map.print_map(game_map,rows,cols)