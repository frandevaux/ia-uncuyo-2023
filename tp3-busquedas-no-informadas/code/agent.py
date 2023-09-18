from collections import deque
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
                return path

            possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for moves in possible_moves:
                new_x, new_y = x + moves[0], y + moves[1]

                if 0 <= new_x < matrix_size and 0 <= new_y < matrix_size and not (new_x, new_y) in visited and \
                        self.env.matrix[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited.append((new_x, new_y))
                    parents[new_x][new_y] = (x, y)

        return []

    def dfs_recursive(self, x, y, visited, parents):
        matrix_size = self.env.matrix_size


        if (x, y) == self.env.goal_position:

            path = []
            while (x, y) != self.env.initial_position:
                path.append((x, y))
                x, y = parents[x][y]
            path.append(self.env.initial_position)
            path.reverse()
            return path

        possibles_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for moves in possibles_moves:
            new_x, new_y = x + moves[0], y + moves[1]

            if (
                    0 <= new_x < matrix_size
                    and 0 <= new_y < matrix_size
                    and not (new_x, new_y) in visited
                    and self.env.matrix[new_x][new_y] == 0
            ):
                visited.append((new_x, new_y))
                parents[new_x][new_y] = (x, y)
                path = self.dfs_recursive(new_x, new_y, visited, parents)
                if path:
                    return path

        return []

    def dfs(self):
        matrix_size = self.env.matrix_size
        visited = []
        parents = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        visited.append(self.env.initial_position)

        path = self.dfs_recursive(
            self.env.initial_position[0], self.env.initial_position[1], visited, parents
        )

        return path

    def ucs(self):
        matrix_size = self.env.matrix_size
        visited = set()
        cost_so_far = [[float('inf')] * matrix_size for _ in range(matrix_size)]
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
                return path

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

        return []

    def ldfs_recursive(self, x, y, visited, parents, depth_limit):
        matrix_size = self.env.matrix_size

        if (x, y) == self.env.goal_position:

            path = []
            while (x, y) != self.env.initial_position:
                path.append((x, y))
                x, y = parents[x][y]
            path.append(self.env.initial_position)
            path.reverse()
            return path

        if depth_limit == 0:
            return []

        possibles_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for moves in possibles_moves:
            new_x, new_y = x + moves[0], y + moves[1]

            if (
                    0 <= new_x < matrix_size
                    and 0 <= new_y < matrix_size
                    and not (new_x, new_y) in visited
                    and self.env.matrix[new_x][new_y] == 0
            ):
                visited.append((new_x, new_y))
                parents[new_x][new_y] = (x, y)
                path = self.ldfs_recursive(
                    new_x, new_y, visited, parents, depth_limit - 1
                )
                if path:
                    return path

        return []

    def ldfs(self, depth_limit):
        matrix_size = self.env.matrix_size
        visited = []
        parents = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        visited.append(self.env.initial_position)

        path = self.ldfs_recursive(
            self.env.initial_position[0], self.env.initial_position[1], visited, parents, depth_limit
        )

        return path
