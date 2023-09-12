from random import randint
from action import Action
from slot import Slot
from color import Color


class Environment:
    def __init__(self, matrixSize: int, initial_position: Slot, goal_position: Slot):
        self.matrix = [[Slot(i, j) for i in range(matrixSize)] for j in range(matrixSize)]
        self.matrixSize = matrixSize
        self.initial_position = initial_position
        self.goal_position = goal_position
        self.init_slots()

    def init_slots(self):

        obstacles_left = 0.08 * self.matrixSize * self.matrixSize
        while obstacles_left > 0:
            x = randint(0, self.matrixSize - 1)
            y = randint(0, self.matrixSize - 1)

            ## Si no es la posicion inicial ni la final
            if (x != self.initial_position.posX and y != self.initial_position.posY and x != self.goal_position.posX and y != self.goal_position.posY):
                self.matrix[x][y].isObstacle = True
                obstacles_left -= 1

    def is_valid_action(self, coord: Slot, action: Action):
        posX = coord.posX
        posY = coord.posY

        match action:
            case Action.DOWN:
                return posY + 1 < self.matrixSize and self.matrix[posX] [posY + 1] == 0
            case Action.UP:
                return posY - 1 >= 0 and self.matrix[posX][ posY - 1] == 0
            case Action.RIGHT:
                return posX + 1 < self.matrixSize and self.matrix[posX + 1][ posY] == 0
            case Action.LEFT:
                return posX - 1 >= 0 and self.matrix[posX - 1][ posY] == 0
            case _:
                return False



    def change_char(self, cell: Slot):

        if (cell.isObstacle == True):
            return "X"
        else:
            return "-"

    def print_environment(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if (i == self.initial_position.posX and j == self.initial_position.posY):
                    print("S", end="")
                elif (i == self.goal_position.posX and j == self.goal_position.posY):
                    print("G", end="")
                else:
                    print(self.change_char(self.matrix[i][j]), end="")
            print()
