import math
import random

from colorama import Fore


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [random.randint(0, size - 1) for _ in range(size)]
        self.conflicts = self.calculate_conflicts()

    def calculate_conflicts(self):
        conflicts = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def move_queen(self, row, new_col):
        self.board[row] = new_col

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i] == j:
                    print(Fore.CYAN + "Q", end=" ")
                else:
                    print(Fore.WHITE + "0", end=" ")
            print()
        print()


def hill_climbing(board, max_iter):
    current_board = board
    current_conflicts = current_board.conflicts
    iteration = 0
    while iteration < max_iter and current_conflicts > 0:
        new_board = Board(board.size)
        row, col = random.sample(range(board.size), 2)
        new_board.move_queen(row, current_board.board[col])
        new_conflicts = new_board.calculate_conflicts()

        if new_conflicts < current_conflicts:
            current_board = new_board
            current_conflicts = new_conflicts

        iteration += 1

    return current_board, current_conflicts, iteration


def simulated_annealing(board, max_iter, initial_temp, cooling_rate):
    current_board = board
    current_conflicts = current_board.conflicts
    iteration = 0
    temp = initial_temp
    while iteration < max_iter and current_conflicts > 0:
        new_board = Board(board.size)
        row, col = random.sample(range(board.size), 2)
        new_board.move_queen(row, current_board.board[col])
        new_conflicts = new_board.calculate_conflicts()
        delta_conflicts = new_conflicts - current_conflicts

        if delta_conflicts <= 0 or random.random() < math.exp(-delta_conflicts / temp):
            current_board = new_board
            current_conflicts = new_conflicts

        aux_temp = temp * cooling_rate
        if aux_temp != 0:
            temp = aux_temp
        iteration += 1

    return current_board, current_conflicts, iteration
