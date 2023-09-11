from random import randint
from action import Action

class Environment:
    def __init__(self, matrixSize: int, initial_position: tuple, goal_position: tuple):
        self.matrix = [[0 for _ in range(matrixSize)] for _ in range(matrixSize)]
        self.matrixSize = matrixSize
        self.initial_position = initial_position
        self.goal_position = goal_position
        self.init_slots ()

    def init_slots(self):

        obstacles_left = 0.08*self.matrixSize*self.matrixSize
        while obstacles_left > 0:
            x = randint(0, self.matrixSize - 1)
            y = randint(0, self.matrixSize - 1)

            if (not self.matrix[x][y] == 1 and not x== self.initial_position[0] and not y== self.initial_position[1] and not x== self.goal_position[0] and not y== self.goal_position[1]):
                self.matrix[x][y] = 1
                obstacles_left -= 1
    
    def is_valid_action(self, coord: tuple, action: Action):
        match action:
            case Action.DOWN:
                return coord[1]+1 < self.matrixSize and self.matrix[coord[0], coord[1]+1] == 0
            case Action.UP:
                return coord[1]-1 >= 0 and self.matrix[coord[0], coord[1]-1] == 0
            case Action.RIGHT:
                return coord[0]+1 < self.matrixSize and self.matrix[coord[0] + 1, coord[1]] == 0
            case Action.LEFT:
                return coord[0]-1 >= 0 and self.matrix[coord[0] -1, coord[1]] == 0
            case _:
                return False

    def is_obstacle(self, posX, posY):
        return self.matrix[posX][posY] == 1
    
    def change_char(self, cell):
        
        if (cell ==0 ):
            return "-"
        elif (cell ==1):
            return "X"
    def print_environment(self):
        for i in range(len(self.matrix)):
            for j in range (len(self.matrix[0])):
                if (i == self.initial_position[0] and j ==self.initial_position[1]):
                    print("S", end="")
                elif (i == self.goal_position[0] and j ==self.goal_position[1]):
                    print("G", end="") 
                else:
                    print(self.change_char(self.matrix[i][j]), end="") 
            print()
        