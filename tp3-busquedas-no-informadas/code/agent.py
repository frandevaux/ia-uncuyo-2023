import random
from collections import deque
from environment import Environment


class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.posX = env.initial_position[0]
        self.posY = env.initial_position[1]
        self.points = 0
        self.remaining_actions = 1000
        self.path = []

    def bfs(self):
        filas, columnas = self.env.matrixSize, self.env.matrixSize
        visitado = [[False for _ in range(columnas)] for _ in range(filas)]
        padres = [[None for _ in range(columnas)] for _ in range(filas)]
        cola = deque()
        cola.append(self.env.initial_position)
        visitado[self.env.initial_position[0]][self.env.initial_position[1]] = True

        while cola:
            fila, columna = cola.popleft()

            # Verificar si hemos llegado al punto final
            if (fila, columna) == self.env.goal_position:
                # Reconstruir el camino
                camino = []
                while (fila, columna) != self.env.initial_position:
                    camino.append((fila, columna))
                    fila, columna = padres[fila][columna]
                camino.append(self.env.initial_position)
                camino.reverse()
                return camino

            # Generar los vecinos posibles (arriba, abajo, izquierda, derecha)
            movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for movimiento in movimientos:
                nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]

                # Verificar si la nueva posición está dentro de la matriz y no es un obstáculo
                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and not visitado[nueva_fila][
                    nueva_columna] and self.env.matrix[nueva_fila][nueva_columna] == 0:
                    cola.append((nueva_fila, nueva_columna))
                    visitado[nueva_fila][nueva_columna] = True
                    padres[nueva_fila][nueva_columna] = (fila, columna)

        # Si no se encuentra un camino, devuelve una lista vacía
        return []



