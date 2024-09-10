from heapq import heappush, heappop
from heuristic import heuristic1

def astar1(puzzle):
    def get_priority(state):
        return heuristic1(state)

    frontier = []
    heappush(frontier, (get_priority(puzzle.board), puzzle.board))
    explored = set()

    while frontier:
        _, current_state = heappop(frontier)

        if puzzle.is_goal(current_state):
            return current_state

        explored.add(tuple(map(tuple, current_state)))

        for move in puzzle.get_possible_moves(current_state):
            car, direction = move
            new_state = puzzle.move_car(current_state, car, direction)

            if tuple(map(tuple, new_state)) not in explored:
                heappush(frontier, (get_priority(new_state), new_state))

    return None