import matplotlib.pyplot as plt
import csv
import time
from board import Board, hill_climbing, simulated_annealing, genetic_algorithm

def run_algorithm(algorithm_func, *args, **kwargs):
    start_time = time.time()
    result = algorithm_func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def boxPlotGenerator(repetitions, csv_filename, image_filename):
    hill_climbing_times = []
    hill_climbing_success = 0

    simulated_annealing_times = []
    simulated_annealing_success = 0


    genetic_algorithm_times = []
    genetic_algorithm_success = 0

    full_data = []

    has_to_graphic = True
    board_sizes = [4,8,10,12,15]
    for board_size in board_sizes:

        print("Board size: " + str(board_size))

        for i in range(repetitions):

            print("Iteration: " + str(i + 1))
            board = Board(board_size)

            result, time_taken = run_algorithm(hill_climbing, board, 5000)
            hill_climbing_times.append(time_taken)
            if result[1] == 0:
                hill_climbing_success += 1
            if has_to_graphic and board_size == 12:
                # Extrae los valores de conflicto y de iteración en listas separadas
                conflicts, iterations = zip(*result[3])

                # Crea el gráfico de cómo cambia el número de conflictos con el paso de las iteraciones
                plt.figure()
                plt.title('Número de conflictos en cada iteración con ' + str(board_size) + ' reinas. Hill Climbing')
                plt.xlabel('Iteración')
                plt.ylabel('Número de conflictos')

                # Grafica el número de conflictos en cada iteración
                plt.plot(iterations, conflicts, marker='o', linestyle='-')

                plt.grid(True)  # Activa la cuadrícula

                plt.savefig("Conflicts_iterations_HC")

                # Muestra el gráfico
                plt.show()
            full_data.append(
                ("Hill Climbing", str(i + 1), str(board_size), str(time_taken), str(result[1]), str(result[2])))

            result, time_taken = run_algorithm(simulated_annealing, board, 5000, 100.0, 0.5)
            simulated_annealing_times.append(time_taken)
            if result[1] == 0:
                simulated_annealing_success += 1
            if has_to_graphic and board_size == 12:
                # Extrae los valores de conflicto y de iteración en listas separadas
                conflicts, iterations = zip(*result[3])

                # Crea el gráfico de cómo cambia el número de conflictos con el paso de las iteraciones
                plt.figure()
                plt.title(
                    'Número de conflictos en cada iteración con ' + str(board_size) + ' reinas. Simulated Annealing')
                plt.xlabel('Iteración')
                plt.ylabel('Número de conflictos')

                # Grafica el número de conflictos en cada iteración
                plt.plot(iterations, conflicts, marker='o', linestyle='-')

                plt.grid(True)  # Activa la cuadrícula

                plt.savefig("Conflicts_iterations_SA")

                # Muestra el gráfico
                plt.show()
            full_data.append(
                ("Simulated Annealing", str(i + 1), str(board_size), str(time_taken), str(result[1]), str(result[2])))

            result, time_taken = run_algorithm(genetic_algorithm, board, 5000, 24, 0.17)
            genetic_algorithm_times.append(time_taken)
            if result[1] == 0:
                genetic_algorithm_success += 1
            if has_to_graphic and board_size == 12:
                # Extrae los valores de conflicto y de iteración en listas separadas
                conflicts, iterations = zip(*result[3])

                # Crea el gráfico de cómo cambia el número de conflictos con el paso de las iteraciones
                plt.figure()
                plt.title(
                    'Número de conflictos en cada iteración con ' + str(board_size) + ' reinas. Algoritmo genético')
                plt.xlabel('Iteración')
                plt.ylabel('Número de conflictos')

                # Grafica el número de conflictos en cada iteración
                plt.plot(iterations, conflicts, marker='o', linestyle='-')

                plt.grid(True)  # Activa la cuadrícula

                plt.savefig("Conflicts_iterations_GA")
                has_to_graphic = False

                # Muestra el gráfico
                plt.show()
            full_data.append(
                ("Genetic Algorithm", str(i + 1), str(board_size), str(time_taken), str(result[1]), str(result[2])))

    data = [hill_climbing_times, simulated_annealing_times, genetic_algorithm_times]

    print()

    print("Hill Climbing success rate: " + str(hill_climbing_success /( repetitions * len(board_sizes))))
    print("Simulated Annealing success rate: " + str(simulated_annealing_success / (repetitions * len(board_sizes))))
    print("Genetic Algorithm success rate: " + str(genetic_algorithm_success / (repetitions * len(board_sizes))))

    print()

    # print average and standard deviation from time taken
    print("Hill Climbing average time: " + str(sum(hill_climbing_times) / len(hill_climbing_times)))
    print("Hill Climbing time standard deviation: " + str((sum([(x - (sum(hill_climbing_times) / len(hill_climbing_times))) ** 2 for x in hill_climbing_times]) / len(hill_climbing_times)) ** 0.5))
    print("Simulated Annealing average time: " + str(sum(simulated_annealing_times) / len(simulated_annealing_times)))
    print("Simulated Annealing time standard deviation: " + str((sum([(x - (sum(simulated_annealing_times) / len(simulated_annealing_times))) ** 2 for x in simulated_annealing_times]) / len(simulated_annealing_times)) ** 0.5))
    print("Genetic Algorithm average time: " + str(sum(genetic_algorithm_times) / len(genetic_algorithm_times)))
    print("Genetic Algorithm time standard deviation: " + str((sum([(x - (sum(genetic_algorithm_times) / len(genetic_algorithm_times))) ** 2 for x in genetic_algorithm_times]) / len(genetic_algorithm_times)) ** 0.5))

    print()

    # print average and standard deviation from number of iterations
    print("Hill Climbing average iterations: " + str(sum([int(x[5]) for x in full_data if x[0] == "Hill Climbing"]) / len([int(x[5]) for x in full_data if x[0] == "Hill Climbing"])))
    print("Hill Climbing iterations standard deviation: " + str((sum([(int(x[5]) - (sum([int(x[5]) for x in full_data if x[0] == "Hill Climbing"]) / len([int(x[5]) for x in full_data if x[0] == "Hill Climbing"]))) ** 2 for x in full_data if x[0] == "Hill Climbing"]) / len([int(x[5]) for x in full_data if x[0] == "Hill Climbing"])) ** 0.5))
    print("Simulated Annealing average iterations: " + str(sum([int(x[5]) for x in full_data if x[0] == "Simulated Annealing"]) / len([int(x[5]) for x in full_data if x[0] == "Simulated Annealing"])))
    print("Simulated Annealing iterations standard deviation: " + str((sum([(int(x[5]) - (sum([int(x[5]) for x in full_data if x[0] == "Simulated Annealing"]) / len([int(x[5]) for x in full_data if x[0] == "Simulated Annealing"]))) ** 2 for x in full_data if x[0] == "Simulated Annealing"]) / len([int(x[5]) for x in full_data if x[0] == "Simulated Annealing"])) ** 0.5))
    print("Genetic Algorithm average iterations: " + str(sum([int(x[5]) for x in full_data if x[0] == "Genetic Algorithm"]) / len([int(x[5]) for x in full_data if x[0] == "Genetic Algorithm"])))
    print("Genetic Algorithm iterations standard deviation: " + str((sum([(int(x[5]) - (sum([int(x[5]) for x in full_data if x[0] == "Genetic Algorithm"]) / len([int(x[5]) for x in full_data if x[0] == "Genetic Algorithm"]))) ** 2 for x in full_data if x[0] == "Genetic Algorithm"]) / len([int(x[5]) for x in full_data if x[0] == "Genetic Algorithm"])) ** 0.5))


    # Guarda los tiempos en un archivo CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Algorithm", "Board_n", "Board size", "Execution Time (s)", "Number of conflicts", "Number of iterations"])
        writer.writerows(full_data)



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
