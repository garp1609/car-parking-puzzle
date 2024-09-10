import os

class CarParkingPuzzle:
    def __init__(self, board):
        self.board = board
        self.player_car = 'A'
        self.goal = '0'

    @staticmethod
    def load_level(level_name):
        levels_dir = 'levels'  # Nombre de la carpeta donde están los niveles

        # Comprobar si la carpeta existe y es un directorio
        if not os.path.isdir(levels_dir):
            raise FileNotFoundError(f"La carpeta '{levels_dir}' no existe o no es un directorio.")

        file_path = os.path.join(levels_dir, level_name)

        # Comprobar si el archivo del nivel existe
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No se encontró el archivo '{level_name}' en la carpeta '{levels_dir}'.")

        with open(file_path, 'r') as file:
            board = [list(line.strip()) for line in file.readlines()]

        return CarParkingPuzzle(board)

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_goal(self, state):
        for row in state:
            if self.goal in row:
                goal_pos = (state.index(row), row.index(self.goal))
                player_pos = (state.index(row), row.index(self.player_car))
                return goal_pos[0] == player_pos[0] and goal_pos[1] == player_pos[1]
        return False

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