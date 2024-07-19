import sys

def end_game():
    print("Game Over")
    sys.exit()

def player_collided(self):
    print("Player ran into enemy")
    print("X = " + str(self.col))
    print("Y = " + str(self.row))
    end_game()

def enemy_defeated():
    print("You have defeat all enemies and saved the world")
    end_game()

def sword_broken():
    print("The enemy has broke the sword all hope is lost")
    end_game()