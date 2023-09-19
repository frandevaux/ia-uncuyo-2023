from collections import deque

import numpy
import math
from environment import Environment
import heapq


def euclidean_distance(x, y):
    x1, y1 = x
    x2, y2 = y
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.posX = env.initial_position[0]
        self.posY = env.initial_position[1]
        self.points = 0
        self.remaining_actions = 1000
        self.path = []



    # Función para realizar la búsqueda A*
    def a_star(self):

        visitado = [[False for _ in range(self.env.matrix_size)] for _ in range(self.env.matrix_size)]
        g = [[numpy.inf for _ in range(self.env.matrix_size)] for _ in range(self.env.matrix_size)]
        f = [[numpy.inf for _ in range(self.env.matrix_size )] for _ in range(self.env.matrix_size )]
        start = self.env.initial_position
        g[start[0]][start[1]] = 0
        f[start[0]][start[1]] = euclidean_distance(start, self.env.goal_position)
        visited_nodes = 1

        # Utilizar una cola de prioridad (heap) para manejar los nodos a expandir
        priority_queue = [(f[start[0]][start[1]], start)]

        while priority_queue:
            _, current_position = heapq.heappop(priority_queue)
            x, y = current_position

            # Verificar si hemos llegado al punto final
            if (x, y) == self.env.goal_position:
                path = []
                while current_position:
                    path.append(current_position)
                    current_position = visitado[current_position[0]][current_position[1]]
                path.reverse()
                return path, visited_nodes

            # Generar los vecinos posibles (arriba, abajo, izquierda, derecha)
            possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for move in possible_moves:
                new_x, new_y = x + move[0], y + move[1]

                # Verificar si la nueva posición está dentro de la matriz y no es un obstáculo
                if (
                        0 <= new_x < self.env.matrix_size
                        and 0 <= new_y < self.env.matrix_size
                        and not visitado[new_x][new_y]
                        and self.env.matrix[new_x][new_y] == 0
                ):
                    nuevo_g = g[x][y] + 1
                    if nuevo_g < g[new_x][new_y]:
                        visited_nodes += 1
                        visitado[new_x][new_y] = current_position
                        g[new_x][new_y] = nuevo_g
                        f[new_x][new_y] = nuevo_g + 2 * euclidean_distance((new_x, new_y), self.env.goal_position)
                        heapq.heappush(priority_queue, (f[new_x][new_y], (new_x, new_y)))

        # Si no se encuentra un camino, devuelve una lista vacía
        return [], visited_nodes

    def bfs(self):
        matrix_size = self.env.matrix_size
        visited = []
        parents = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        queue = deque()
        queue.append(self.env.initial_position)
        visited.append(self.env.initial_position)

        while queue:
            x, y = queue.popleft()

            if (x, y) == self.env.goal_position:

                path = []
                while (x, y) != self.env.initial_position:
                    path.append((x, y))
                    x, y = parents[x][y]
                path.append(self.env.initial_position)
                path.reverse()
                return path, len(visited)

            possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for moves in possible_moves:
                new_x, new_y = x + moves[0], y + moves[1]

                if 0 <= new_x < matrix_size and 0 <= new_y < matrix_size and not (new_x, new_y) in visited and \
                        self.env.matrix[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited.append((new_x, new_y))
                    parents[new_x][new_y] = (x, y)

        return [], len(visited)

    def dfs(self):
        matrix_size = self.env.matrix_size
        visited = set()
        parents = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        stack = [(self.env.initial_position, None)]  # La tupla contiene (nodo, nodo padre)

        while stack:
            current_node, parent_node = stack.pop()

            x, y = current_node

            if current_node == self.env.goal_position:
                # Reconstruir el camino
                path = []
                while current_node != self.env.initial_position:
                    path.append(current_node)
                    current_node = parents[x][y]
                    x, y = current_node
                path.append(self.env.initial_position)
                path.reverse()
                return path, len(visited)

            if current_node in visited:
                continue

            visited.add(current_node)

            possibles_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for moves in possibles_moves:
                new_x, new_y = x + moves[0], y + moves[1]

                if (
                    0 <= new_x < matrix_size
                    and 0 <= new_y < matrix_size
                    and not (new_x, new_y) in visited
                    and self.env.matrix[new_x][new_y] == 0
                ):
                    stack.append(((new_x, new_y), current_node))
                    parents[new_x][new_y] = current_node

        return [], len(visited)


    def ucs(self):
        matrix_size = self.env.matrix_size
        visited = set()
        cost_so_far = [[numpy.inf] * matrix_size for _ in range(matrix_size)]
        cost_so_far[self.env.initial_position[0]][self.env.initial_position[1]] = 0
        priority_queue = [(0, self.env.initial_position)]
        heapq.heapify(priority_queue)
        self.path = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]

        while priority_queue:
            cost, (x, y) = heapq.heappop(priority_queue)

            if (x, y) == self.env.goal_position:

                path = []
                while (x, y) != self.env.initial_position:
                    path.append((x, y))
                    x, y = self.path[x][y]
                path.append(self.env.initial_position)
                path.reverse()
                return path, len(visited)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            possibles_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for moves in possibles_moves:
                new_x, new_y = x + moves[0], y + moves[1]

                if 0 <= new_x < matrix_size and 0 <= new_y < matrix_size and self.env.matrix[new_x][new_y] == 0:
                    new_cost = cost + 1

                    if new_cost < cost_so_far[new_x][new_y]:
                        cost_so_far[new_x][new_y] = new_cost
                        heapq.heappush(priority_queue, (new_cost, (new_x, new_y)))
                        self.path[new_x][new_y] = (x, y)

        return [], len(visited)

    def ldfs(self, depth_limit):
        matrix_size = self.env.matrix_size
        visited = set()
        parents = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        stack = [(self.env.initial_position, None, 0)]  # La tupla contiene (nodo, nodo padre, profundidad actual)

        while stack:
            current_node, parent_node, depth = stack.pop()

            x, y = current_node

            if current_node == self.env.goal_position:
                # Reconstruir el camino
                path = []
                while current_node != self.env.initial_position:
                    path.append(current_node)
                    current_node = parents[x][y]
                    x, y = current_node
                path.append(self.env.initial_position)
                path.reverse()
                return path, len(visited)

            if current_node in visited or depth == depth_limit:
                continue

            visited.add(current_node)

            possibles_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for moves in possibles_moves:
                new_x, new_y = x + moves[0], y + moves[1]

                if (
                    0 <= new_x < matrix_size
                    and 0 <= new_y < matrix_size
                    and not (new_x, new_y) in visited
                    and self.env.matrix[new_x][new_y] == 0
                ):
                    stack.append(((new_x, new_y), current_node, depth + 1))
                    parents[new_x][new_y] = current_node

        return [], len(visited)