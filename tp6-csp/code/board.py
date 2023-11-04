class BacktrackingSolver:
    def __init__(self, n):
        self.n_queens = n
        self.solution = None
        self.step_count = 0

    def safe_position(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solver(self, board, row):
        if row == self.n_queens:
            self.solution = list(board)
            return
        for col in range(self.n_queens):
            self.step_count += 1
            if self.safe_position(board, row, col):
                board[row] = col
                self.solver(board, row + 1)
                if self.solution:
                    return

    def find_solution(self):
        board = [-1] * self.n_queens
        self.solver(board, 0)

    def print_solution(self):
        for row in range(self.n_queens):
            for col in range(self.n_queens):
                if self.solution[row] == col:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()

    def calculate_conflicts(self, board):
        conflicts = 0
        for row in range(self.n_queens):
            for col in range(self.n_queens):
                if board[row] == col:
                    continue
                if board[row] - row == col - row or \
                        board[row] + row == col + row:
                    conflicts += 1
        return conflicts

    def run(self):
        self.find_solution()
        return self.solution, self.step_count


class ForwardCheckingSolver:
    def __init__(self, n):
        self.n_queens = n
        self.solution = None
        self.domains = {}  # Diccionario para rastrear el dominio de cada variable
        self.step_count = 0

    def safe_position(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def forward_check(self, board, row, col):
        for i in range(row + 1, self.n_queens):
            if i in self.domains:
                if col in self.domains[i]:
                    self.domains[i].remove(col)
                diagonal1 = col + (i - row)
                if diagonal1 in self.domains[i]:
                    self.domains[i].remove(diagonal1)
                diagonal2 = col - (i - row)
                if diagonal2 in self.domains[i]:
                    self.domains[i].remove(diagonal2)

    def solver(self, board, row):
        if row == self.n_queens:
            self.solution = list(board)
            return

        if row not in self.domains:
            self.domains[row] = set(range(self.n_queens))

        min_domain_variable = min(self.domains, key=lambda var: len(self.domains[var]))

        for col in self.domains[min_domain_variable]:
            if self.safe_position(board, row, col):
                board[row] = col
                original_domains = self.domains.copy()
                self.forward_check(board, row, col)
                self.solver(board, row + 1)
                if self.solution:
                    return
                self.domains = original_domains
                self.step_count += 1

    def find_solution(self):
        board = [-1] * self.n_queens
        self.solver(board, 0)

    def run(self):
        self.find_solution()
        return self.solution, self.step_count

    def print_solution(self):
        for row in range(self.n_queens):
            for col in range(self.n_queens):
                if self.solution[row] == col:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()

    def calculate_conflicts(self, board):
        conflicts = 0
        for row in range(self.n_queens):
            for col in range(self.n_queens):
                if board[row] == col:
                    continue
                if board[row] - row == col - row or \
                        board[row] + row == col + row:
                    conflicts += 1
        return conflicts
