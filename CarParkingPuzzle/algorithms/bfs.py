from collections import deque

def bfs(puzzle):
    start_state = puzzle.board
    frontier = deque([start_state])
    explored = set()
    
    while frontier:
        state = frontier.popleft()
        if puzzle.is_goal(state):
            return state
        
        explored.add(tuple(map(tuple, state)))
        for move in puzzle.get_possible_moves(state):
            new_state = puzzle.move_car(state, *move)
            if tuple(map(tuple, new_state)) not in explored:
                frontier.append(new_state)
    
    return None