class NQueensBacktrackingSolver:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.step = 0

    def is_safe(self, board, row, col):
        # Función para verificar si es seguro colocar una reina en la posición (row, col)
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(self, board, row):
        # Función recursiva para encontrar la primera solución
        if row == self.n:
            self.solution = list(board)
            return
        for col in range(self.n):
            self.step += 1
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve(board, row + 1)
                if self.solution:
                    return

    def find_solution(self):
        board = [-1] * self.n
        self.solve(board, 0)

    def print_solution(self):
        # Función para imprimir la solución
        for row in range(self.n):
            for col in range(self.n):
                if self.solution[row] == col:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
        
    def calculate_conflicts(self, board):
        # Función para calcular la cantidad de conflictos en el tablero
        conflicts = 0
        for row in range(self.n):
            for col in range(self.n):
                if board[row] == col:
                    continue
                if board[row] - row == col - row or \
                   board[row] + row == col + row:
                    conflicts += 1
        return conflicts
    def run(self):
        self.find_solution()
        return self.solution, self.step
    

class NQueensForwardCheckingSolver:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.domains = {}  # Diccionario para rastrear el dominio de cada variable
        self.step = 0

    def is_safe(self, board, row, col):
        # Función para verificar si es seguro colocar una reina en la posición (row, col)
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def forward_check(self, board, row, col):
        # Función para realizar la propagación y reducir los dominios
        for i in range(row + 1, self.n):
            if i in self.domains:
                if col in self.domains[i]:
                    self.domains[i].remove(col)
                diagonal1 = col + (i - row)
                if diagonal1 in self.domains[i]:
                    self.domains[i].remove(diagonal1)
                diagonal2 = col - (i - row)
                if diagonal2 in self.domains[i]:
                    self.domains[i].remove(diagonal2)

    def solve(self, board, row):
        if row == self.n:
            self.solution = list(board)
            return

        if row not in self.domains:
            self.domains[row] = set(range(self.n))

        # Seleccionar la variable con el dominio más restrictivo (menos valores en el dominio)
        min_domain_variable = min(self.domains, key=lambda var: len(self.domains[var]))

        for col in self.domains[min_domain_variable]:
            if self.is_safe(board, row, col):
                board[row] = col
                original_domains = self.domains.copy()
                self.forward_check(board, row, col)
                self.solve(board, row + 1)
                if self.solution:
                    return
                self.domains = original_domains
                self.step += 1

    def find_solution(self):
        board = [-1] * self.n
        self.solve(board, 0)

    def run(self):
        self.find_solution()
        return self.solution, self.step

    def print_solution(self):
        # Función para imprimir la solución
        for row in range(self.n):
            for col in range(self.n):
                if self.solution[row] == col:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
    
    def calculate_conflicts(self, board):
        # Función para calcular la cantidad de conflictos en el tablero
        conflicts = 0
        for row in range(self.n):
            for col in range(self.n):
                if board[row] == col:
                    continue
                if board[row] - row == col - row or \
                   board[row] + row == col + row:
                    conflicts += 1
        return conflicts