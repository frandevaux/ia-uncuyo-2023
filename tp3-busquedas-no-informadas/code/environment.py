from random import randint
from colorama import Fore





class Environment:
    def __init__(self, matrixSize: int, initial_position: tuple, goal_position: tuple):
        self.matrix = [[0 for _ in range(matrixSize)] for _ in range(matrixSize)]
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
            if ((x,y) != self.initial_position and (x,y) != self.goal_position and self.matrix[x][y] == 0):
                self.matrix[x][y] = 1
                obstacles_left -= 1


    def print_environment(self, camino = None):
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                if (i, j) == self.initial_position:
                    print(Fore.GREEN + "I", end=" ")
                elif (i, j) == self.goal_position:
                    print(Fore.GREEN + "F", end=" ")
                elif camino != None and (i, j) in camino:
                    print(Fore.YELLOW + "0", end=" ")
                elif self.matrix[i][j] == 1:
                    print(Fore.RED + "X", end=" ")
                else:
                    print(Fore.LIGHTWHITE_EX + "0", end=" ")
            print()
        print()