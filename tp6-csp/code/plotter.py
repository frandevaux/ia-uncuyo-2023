import matplotlib.pyplot as plt
import time

from board import BacktrackingSolver, ForwardCheckingSolver

solver = ForwardCheckingSolver(15)
board, steps = solver.run()
solver.print_solution()

print(steps)
print(solver.calculate_conflicts(board))

solver = BacktrackingSolver(15)
board, steps = solver.run()
solver.print_solution()

print(steps)
print(solver.calculate_conflicts(board))


def run_algorithm(algorithm_func,n):
    start_time = time.time()
    solver = algorithm_func(n)
    board, steps = solver.run()
    end_time = time.time()
    execution_time = end_time - start_time
    return board,steps, execution_time

def boxPlotGenerator():
    backtracking_times = []
    forwardchecking_times = []

    backtracking_steps = []
    forwardchecking_steps = []

    
    board_sizes = [4,8,10,12,15]
    for board_size in board_sizes:

        print("Board size: " + str(board_size))

        board, steps, execution_time = run_algorithm(BacktrackingSolver, board_size)
        backtracking_times.append(execution_time)
        backtracking_steps.append(steps)

        board, steps, execution_time = run_algorithm(ForwardCheckingSolver, board_size)
        forwardchecking_times.append(execution_time)
        forwardchecking_steps.append(steps)

    # Genera el gráfico
    data = [backtracking_times, forwardchecking_times]


    fig, ax = plt.subplots()
    ax.set_title('Comparación de algoritmos de CSP por tiempo de ejecución')
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Tiempo de ejecución (s)')

    # Utiliza patch_artist=True para habilitar la configuración de colores
    boxplot = ax.boxplot(data, patch_artist=True)

    # Define colores para las cajas
    colors = ['#FFB6C1', '#87CEEB']  # Agrega más colores si es necesario
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_xticklabels(['Backtracking', 'Forward Checking'])

    

    # Muestra el gráfico
    plt.show()

    # Guardar el grafico
    fig.savefig('boxplot_time.png')

    # Genera el gráfico
    data = [backtracking_steps, forwardchecking_steps]


    fig, ax = plt.subplots()
    ax.set_title('Comparación de algoritmos de CSP por cantidad de pasos')
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Cantidad de pasos')

    # Utiliza patch_artist=True para habilitar la configuración de colores
    boxplot = ax.boxplot(data, patch_artist=True)

    # Define colores para las cajas
    colors = ['#FFB6C1', '#87CEEB']  # Agrega más colores si es necesario
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)
    
    ax.set_xticklabels(['Backtracking', 'Forward Checking'])

    # Muestra el gráfico
    plt.show()

    # Guardar el grafico
    fig.savefig('boxplot_steps.png')