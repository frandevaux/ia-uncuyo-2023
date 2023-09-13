from random import randint
from action import Action
from slot import Slot
from color import Color


class Environment:
    def __init__(self, matrixSize: int, initial_position: tuple, goal_position: tuple):
        self.matrix = [[Slot(i, j) for i in range(matrixSize)] for j in range(matrixSize)]
        self.matrixSize = matrixSize
        self.initial_position = self.matrix[initial_position[0]][initial_position[1]]
        self.goal_position = self.matrix[goal_position[0]][goal_position[1]]
        self.init_slots()

    def init_slots(self):

        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                self.adjacent_slots(self.matrix[i][j])


        obstacles_left = 0.08 * self.matrixSize * self.matrixSize
        while obstacles_left > 0:
            x = randint(0, self.matrixSize - 1)
            y = randint(0, self.matrixSize - 1)

            ## Si no es la posicion inicial ni la final
            if (x != self.initial_position.posX and y != self.initial_position.posY and x != self.goal_position.posX and y != self.goal_position.posY):
                self.matrix[x][y].isObstacle = True
                obstacles_left -= 1

    def adjacent_slots(self, slot: Slot):
        adjacentSlots = []
        if (slot.posX + 1 < self.matrixSize and self.matrix[slot.posX + 1][slot.posY].isObstacle == False):
            adjacentSlots.append(self.matrix[slot.posX + 1][slot.posY])
        if (slot.posX - 1 >= 0 and self.matrix[slot.posX - 1][slot.posY].isObstacle == False) :
            adjacentSlots.append(self.matrix[slot.posX - 1][slot.posY])
        if (slot.posY + 1 < self.matrixSize and self.matrix[slot.posX][slot.posY + 1].isObstacle == False):
            adjacentSlots.append(self.matrix[slot.posX][slot.posY + 1])
        if (slot.posY - 1 >= 0 and self.matrix[slot.posX][slot.posY - 1].isObstacle == False):
            adjacentSlots.append(self.matrix[slot.posX][slot.posY - 1])

        slot.adjacentSlots = adjacentSlots
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
