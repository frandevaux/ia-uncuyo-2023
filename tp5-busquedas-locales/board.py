import math
import random

from colorama import Fore


class Board:
    def __init__(self, size, board=None):
        self.size = size
        self.board = board or [random.randint(0, size - 1) for _ in range(size)]
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

def generate_initial_population(board, population_size):
    return [Board(board.size) for _ in range(population_size)]

def genetic_algorithm(board, max_iter, population_size, mutation_rate):
    population = generate_initial_population(board, population_size)
    iteration = 0
    while iteration < max_iter:
        population.sort(key=lambda x: x.conflicts)
        if population[0].conflicts == 0:
            return population[0], population[0].conflicts, iteration

        new_population = []

        for i in range(population_size):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                row, col = random.sample(range(board.size), 2)
                child.move_queen(row, col)
                child.conflicts = child.calculate_conflicts()  # Actualizar aptitud

            new_population.append(child)

        population = new_population
        iteration += 1

    population.sort(key=lambda x: x.conflicts)
    best_solution = population[0]
    return best_solution, best_solution.conflicts, iteration

def select_parents(population):
    parents = []
    tournament_candidates = random.sample(population, random.randint(2, len(population)))
    tournament_candidates.sort(key=lambda x: x.conflicts)
    parents.append(tournament_candidates[0])
    parents.append(tournament_candidates[1])
    return parents

def crossover(parent1, parent2):
    crossing_point = random.randint(0, parent1.size - 1)
    child_board = parent1.board[:crossing_point] + parent2.board[crossing_point:]
    return Board(parent1.size, child_board)
