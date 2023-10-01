import matplotlib.pyplot as plt
import csv
import time
from board import Board, hill_climbing, simulated_annealing, genetic_algorithm

def run_algorithm(algorithm_func, *args, **kwargs):
    start_time = time.time()
    result = algorithm_func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result[1], execution_time

def boxPlotGenerator(repetitions, csv_filename, image_filename, board_size):
    hill_climbing_times = []
    simulated_annealing_times = []
    genetic_algorithm_times = []

    for i in range(repetitions):
        print("Iteration: " + str(i + 1))
        board = Board(board_size)

        conflicts, time_taken = run_algorithm(hill_climbing, board, 5000)
        hill_climbing_times.append(time_taken)

        conflicts, time_taken = run_algorithm(simulated_annealing, board, 5000, 100.0, 0.5)
        simulated_annealing_times.append(time_taken)

        conflicts, time_taken = run_algorithm(genetic_algorithm, board, 5000, 24, 0.17)
        genetic_algorithm_times.append(time_taken)

    data = [hill_climbing_times, simulated_annealing_times, genetic_algorithm_times]

    # Guarda los tiempos en un archivo CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Algorithm", "Board_n", "Board size", "Execution Time (s)", "Number of iterations"])
        # Agrega aquí la lógica para escribir los datos completos si es necesario

    fig, ax = plt.subplots()
    ax.set_title('Comparación de algoritmos de búsqueda local por tiempo de ejecución')
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Tiempo de ejecución (s)')

    # Utiliza patch_artist=True para habilitar la configuración de colores
    boxplot = ax.boxplot(data, patch_artist=True)

    # Define colores para las cajas
    colors = ['#FFB6C1', '#87CEEB', '#98FB98']  # Agrega más colores si es necesario
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_xticklabels(['Hill Climbing', 'Simulated Annealing', 'Genetic Algorithm'])

    # Guarda la imagen del gráfico en un archivo
    plt.savefig(image_filename)

    # Muestra el gráfico
    plt.show()
