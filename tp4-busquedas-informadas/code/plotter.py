import matplotlib.pyplot as plt
import numpy as np
import csv  # Importa la biblioteca csv
from environment import Environment
from agent import Agent


def boxPlotGenerator(repetitions, csv_filename, image_filename):
    bfs_results = []
    dfs_results = []
    ucs_results = []
    ldfs_results = []
    astar_results = []
    full_results = []

    for i in range(repetitions):
        # Randomize initial and goal positions
        initial_position = (np.random.randint(0, 100), np.random.randint(0, 100))
        goal_position = (np.random.randint(0, 100), np.random.randint(0, 100))
        env = Environment(100, initial_position, goal_position)
        agent = Agent(env)
        result = agent.bfs()
        full_results.append(("BFS", i + 1, result[1], result[0] != []))
        bfs_results.append(result[1])

        result = agent.dfs()
        full_results.append(("DFS", i + 1, result[1], result[0] != []))
        dfs_results.append(result[1])

        result = agent.ucs()
        full_results.append(("UCS", i + 1 , result[1], result[0] != []))
        ucs_results.append(result[1])

        result = agent.ldfs(5000)
        full_results.append(("LDFS", i + 1, result[1], result[0] != []))
        ldfs_results.append(result[1])

        result = agent.a_star()
        full_results.append(("A*", i + 1, result[1], result[0] != []))
        astar_results.append(result[1])

    data = [bfs_results, dfs_results, ucs_results, ldfs_results, astar_results]

    # Guarda los datos en un archivo CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Agent", "env_n", "explored_states", "success"])
        writer.writerows(full_results)

    fig, ax = plt.subplots()
    ax.set_title('Comparación de algoritmos de búsqueda')
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Cantidad de nodos visitados')

    # Utiliza patch_artist=True para habilitar la configuración de colores
    boxplot = ax.boxplot(data, patch_artist=True)

    # Define colores para las cajas
    colors = ['#FFB6C1', '#87CEEB', '#98FB98', '#FFFF99', '#E6E6FA']
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_xticklabels(['BFS', 'DFS', 'UCS', 'LDFS', 'A*'])

    # Guarda la imagen del gráfico en un archivo
    plt.savefig(image_filename)

    # Muestra el gráfico
    plt.show()


