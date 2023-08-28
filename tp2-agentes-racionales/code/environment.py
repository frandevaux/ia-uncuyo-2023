from random import randint
from enum import Enum

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    CLEAN = 5
    IDLE = 6

class Environment:
    def __init__(self, sizeX, sizeY, dirt_rate):
        self.matrix = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.remaining_dirty_slots = dirt_rate * sizeX * sizeY
        self.init_slots ()

    def init_slots(self):

        dirty_slots_left = self.remaining_dirty_slots
        while dirty_slots_left > 0:
            x = randint(0, self.sizeX - 1)
            y = randint(0, self.sizeY - 1)
            
            if (not self.matrix[x][y]):
                self.matrix[x][y] = 1
                dirty_slots_left -= 1
    
    def is_valid_action(self, agent, action):
        match action:
            case Action.DOWN:
                return agent.posY+1 < self.sizeY
            case Action.UP:
                return agent.posY-1 >= 0
            case Action.RIGHT:
                return agent.posX+1 < self.sizeX
            case Action.LEFT:
                return agent.posX-1 >= 0
            case Action.CLEAN:
                return True 
            case _:
                return False

    def clean_slot(self, posX, posY):
        if (self.is_dirty(posX, posY)):
            self.matrix[posX][posY] = 0
            self.remaining_dirty_slots -= 1

    def is_dirty(self, posX, posY):
        return self.matrix[posX][posY]
    
    def print_environment(self):
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))