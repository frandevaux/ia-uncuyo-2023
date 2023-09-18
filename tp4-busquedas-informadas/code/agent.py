from collections import deque

import numpy

from environment import Environment
import heapq


class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.posX = env.initial_position[0]
        self.posY = env.initial_position[1]
        self.points = 0
        self.remaining_actions = 1000
        self.path = []

    def astar(self):
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

                    # Estimación heurística (en este caso, distancia Manhattan)
                    heuristic = abs(new_x - self.env.goal_position[0]) + abs(new_y - self.env.goal_position[1])

                    priority = new_cost + heuristic

                    if new_cost < cost_so_far[new_x][new_y]:
                        cost_so_far[new_x][new_y] = new_cost
                        heapq.heappush(priority_queue, (priority, (new_x, new_y)))
                        self.path[new_x][new_y] = (x, y)

        return [], len(visited)

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