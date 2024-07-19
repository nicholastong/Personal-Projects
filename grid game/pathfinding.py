import heapq
import entity
import move

def chase(target, chaser):
    if target.row < chaser.row:
        move.move_up(chaser, chaser.game_map)
        return
    elif target.row > chaser.row:
        move.move_down(chaser, chaser.game_map)
        return
    
    # if already on same row
    if target.col < chaser.col:
        move.move_left(chaser, chaser.game_map)
        return
    elif target.col > chaser.col:
        move.move_right(chaser, chaser.game_map)
        return