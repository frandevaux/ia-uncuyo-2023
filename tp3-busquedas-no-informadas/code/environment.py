from random import randint
from colorama import Fore


class Environment:
    def __init__(self, matrix_size: int, initial_position: tuple, goal_position: tuple):
        self.matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
        self.matrix_size = matrix_size
        self.initial_position = initial_position
        self.goal_position = goal_position
        self.init_slots()

    def init_slots(self):

        obstacles_left = 0.08 * self.matrix_size * self.matrix_size
        while obstacles_left > 0:
            x = randint(0, self.matrix_size - 1)
            y = randint(0, self.matrix_size - 1)

            if (x, y) != self.initial_position and (x, y) != self.goal_position and self.matrix[x][y] == 0:
                self.matrix[x][y] = 1
                obstacles_left -= 1

    def print_environment(self, camino=None, current_position=None):

        for i in range(self.matrix_size):
            for j in range(self.matrix_size):

                if current_position is not None and (i, j) == current_position:
                    print(Fore.CYAN + "0", end=" ")
                elif (i, j) == self.initial_position:
                    print(Fore.GREEN + "I", end=" ")
                elif (i, j) == self.goal_position:
                    print(Fore.GREEN + "F", end=" ")
                elif camino is not None and (i, j) in camino:
                    print(Fore.YELLOW + "0", end=" ")
                elif self.matrix[i][j] == 1:
                    print(Fore.RED + "X", end=" ")
                else:
                    print(Fore.LIGHTWHITE_EX + "0", end=" ")
            print()
        print()
