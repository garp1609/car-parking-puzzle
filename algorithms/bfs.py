from collections import deque

def bfs(puzzle):
    queue = deque([(puzzle.board, [])])
    explored = set()

    while queue:
        state, path = queue.popleft()
        if puzzle.is_goal(state):
            return path
        explored.add(tuple(map(tuple, state)))

        for move in puzzle.get_possible_moves(state):
            new_state = puzzle.move_car(state, move[0], move[1])
            if tuple(map(tuple, new_state)) not in explored:
                queue.append((new_state, path + [(move[0], move[1])]))

    return None