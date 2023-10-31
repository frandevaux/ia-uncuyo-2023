import random

from board import Board, hill_climbing, simulated_annealing, genetic_algorithm, backtracking_solver

tablero = Board(15)
tablero.print_board()
print(tablero.conflicts)
result = backtracking_solver(tablero)
result.print_board()
print(result.calculate_conflicts())


"""from plotter import boxPlotGenerator

for i in range(1):
    boxPlotGenerator(30, 'results_iteration_' + str(i+1) +'.csv', 'boxplot' + str(i+1) + '.png')

"""