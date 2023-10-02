import random

from board import Board, hill_climbing, simulated_annealing, genetic_algorithm

"""tablero = Board(15)
tablero.print_board()
print(tablero.conflicts)
result = hill_climbing(tablero,5000)
print( result)
result[0].print_board()

result = simulated_annealing(tablero,5000,100.0,0.5)
print( result)
result[0].print_board()

result = genetic_algorithm(tablero,5000,24,0.17)



print( result)
result[0].print_board()"""

from plotter import boxPlotGenerator

for i in range(1):
    boxPlotGenerator(30, 'results_iteration_' + str(i+1) +'.csv', 'boxplot' + str(i+1) + '.png')

