from board import Board, hill_climbing, simulated_annealing

tablero = Board(5)
tablero.print_board()
print(tablero.conflicts)
result = hill_climbing(tablero,2000)
print( result)
result[0].print_board()

result = simulated_annealing(tablero,2000,100.0,0.5)
print( result)
result[0].print_board()
