import os

class GameState:
    def __init__(self, board, car_positions, moves=0, parent=None):
        self.board = board
        self.car_positions = car_positions
        self.moves = moves
        self.parent = parent     

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def is_goal(self, target_pos):
        return self.board[target_pos[0]][target_pos[1]] == 'A'

    def get_successors(self):
        successors = []
        for car in self.car_positions:
            for move in ['up', 'down', 'left', 'right']:
                new_board = [row[:] for row in self.board]
                new_car_positions = {k: [pos[:] for pos in v] for k, v in self.car_positions.items()}
                if self.move_car(new_board, new_car_positions, car, move):
                    successors.append(GameState(new_board, new_car_positions, self.moves + 1, self))
        return successors

    def move_car(self, board, car_positions, car, direction):
        def move_positions(positions, direction):
            if direction == 'up':
                return [(pos[0] - 1, pos[1]) for pos in positions]
            elif direction == 'down':
                return [(pos[0] + 1, pos[1]) for pos in positions]
            elif direction == 'left':
                return [(pos[0], pos[1] - 1) for pos in positions]
            elif direction == 'right':
                return [(pos[0], pos[1] + 1) for pos in positions]

        positions = car_positions[car]
        new_positions = move_positions(positions, direction)

        for pos in new_positions:
            if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0]) or board[pos[0]][pos[1]] != '.':
                return False

        for pos in positions:
            board[pos[0]][pos[1]] = '.'
        for pos in new_positions:
            board[pos[0]][pos[1]] = car

        car_positions[car] = new_positions
        return True

class CarParkingPuzzle:
    def __init__(self, board):
        self.board = board
        self.player_car = 'A'
        self.goal = '0'

    @staticmethod
    def load_level(level_name):
        levels_dir = 'C:\\Users\\guill\\OneDrive\\Documentos\\CarParkingPuzzle\\levels'

        if not os.path.isdir(levels_dir):
            raise FileNotFoundError(f"La carpeta '{levels_dir}' no existe o no es un directorio.")

        file_path = os.path.join(levels_dir, level_name)

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No se encontró el archivo '{level_name}' en la carpeta '{levels_dir}'.")

        with open(file_path, 'r') as file:
            board = [list(line.strip()) for line in file.readlines()]

        car_positions = {}
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell not in ('.', '0'):
                    if cell not in car_positions:
                        car_positions[cell] = []
                    car_positions[cell].append((i, j))

        return GameState(board, car_positions)

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_goal(self, state):
        player_pos = None
        goal_pos = None

        for i, row in enumerate(state):
            if self.player_car in row:
                player_pos = (i, row.index(self.player_car))
            if self.goal in row:
                goal_pos = (i, row.index(self.goal))

        if player_pos is None or goal_pos is None:
            return False

        return player_pos == goal_pos

    def get_possible_moves(self, state):
        def find_car_positions(state, car):
            positions = []
            for i, row in enumerate(state):
                for j, cell in enumerate(row):
                    if cell == car:
                        positions.append((i, j))
            return positions

        def can_move(state, car, direction):
            positions = find_car_positions(state, car)
            if direction == 'up':
                return all(pos[0] > 0 and state[pos[0] - 1][pos[1]] == '.' for pos in positions)
            elif direction == 'down':
                return all(pos[0] < len(state) - 1 and state[pos[0] + 1][pos[1]] == '.' for pos in positions)
            elif direction == 'left':
                return all(pos[1] > 0 and state[pos[0]][pos[1] - 1] == '.' for pos in positions)
            elif direction == 'right':
                return all(pos[1] < len(state[0]) - 1 and state[pos[0]][pos[1] + 1] == '.' for pos in positions)
            return False

        moves = []
        cars = {cell for row in state for cell in row if cell not in ('.', self.goal)}
        directions = ['up', 'down', 'left', 'right']

        for car in cars:
            for direction in directions:
                if can_move(state, car, direction):
                    moves.append((car, direction))

        return moves

    def move_car(self, state, car, direction):
        def move_positions(positions, direction):
            if direction == 'up':
                return [(pos[0] - 1, pos[1]) for pos in positions]
            elif direction == 'down':
                return [(pos[0] + 1, pos[1]) for pos in positions]
            elif direction == 'left':
                return [(pos[0], pos[1] - 1) for pos in positions]
            elif direction == 'right':
                return [(pos[0], pos[1] + 1) for pos in positions]

        new_state = [row[:] for row in state]
        positions = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == car]
        new_positions = move_positions(positions, direction)

        for pos in positions:
            new_state[pos[0]][pos[1]] = '.'
        for pos in new_positions:
            new_state[pos[0]][pos[1]] = car

        return new_state

    def solve(self, algorithm):
        return algorithm(self)