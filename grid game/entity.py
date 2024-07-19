import constants
import random
import move
import end_game
import pathfinding

class Entity:
    def  __init__(self, row, col, entities, game_map):
        self.row = row
        self.col = col
        self.entities = entities
        self.game_map = game_map
    
    def display(self):
        pass # placeholder

    def tick(self):
        pass # placeholder

    def on_collide(self, type):
        pass # placeholder

def spawn_entity(row, col, map, entities, Type):
    while (True):
            rand_row = random.randint(0, row - 1)
            rand_col = random.randint(0, col - 1)
        # retry if tile occupied
            if type(map[rand_row][rand_col]) == Empty:
                map[rand_row][rand_col] = Type(rand_row, rand_col, entities, map)
                break
    return map[rand_row][rand_col]

####################################################################

class Player(Entity):
    def  __init__(self, row, col, entities, game_map):
        super().__init__(row, col, entities, game_map)
        self.health = constants.PLAYER_HEALTH
        self.has_sword = False
        self.flash = None
        self.has_flash = False
    
    def display(self):
        return constants.PLAYER
    
    def on_collide(self, type):
        if self.has_sword == False and type == Enemy:
            end_game.player_collided(self)
        elif self.has_sword == True and type == Enemy:
            end_game.enemy_defeated()
        elif type == Sword:
            self.has_sword = True
        

def innit_player(row, col, map, entities):
    player = Player(random.randint(0, row - 1), random.randint(0, col - 1), entities, map)
    move.update_location(player, map)
    return player

####################################################################

class Empty(Entity):
    def  __init__(self, row, col, entities, game_map):
        super().__init__(row, col, entities, game_map)
        self.health = 1
    
    def display(self):
        return constants.EMPTY

####################################################################

class Enemy(Entity):
    def  __init__(self, row, col, entities, game_map):
        super().__init__(row, col, entities, game_map)
        self.health = 1
    
    def display(self):
        return constants.ENEMY
    
    def tick(self):
        # retrieve player
        player = None
        for entity in self.entities:
            if type(entity) == Player:
                player = entity

        if player.has_sword == False:
            pathfinding.chase(player, self)
    
    def on_collide(self, object_type):
        if object_type == Player:
             # retrieve player
            player = None
            for entity in self.entities:
                if type(entity) == Player:
                    player = entity
            
            if player.has_sword:
                end_game.enemy_defeated()
            else:
                end_game.player_collided(self)
        elif object_type == Sword:
            end_game.sword_broken()

def innit_enemy(row, col, map, entities):
    return spawn_entity(row, col, map, entities, Enemy)

####################################################################

class Sword(Entity):
    def  __init__(self, row, col, entities, game_map):
        super().__init__(row, col, entities, game_map)
        self.health = 1

    def display(self):
        return constants.SWORD

def innit_sword(row, col, map, entities):
    return spawn_entity(row, col, map, entities, Sword)

####################################################################
class Flash(Entity):
    def  __init__(self, row, col, entities, game_map):
        super().__init__(row, col, entities, game_map)
        self.health = 1

    def display(self):
        return constants.FLASH

def innit_flash(row, col, map, entities):
    map[row][col] = Flash(row, col, entities, map)
    return map[row][col]