import heapq
import math

def astar(initial_state, goal_pos, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(initial_state, goal_pos), initial_state))
    closed_list = set()
    nodes_expanded = 0
    max_depth = 0

    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state.is_goal(goal_pos):
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            path.reverse()
            return path
        
        closed_list.add(current_state)
        nodes_expanded += 1

        for successor in current_state.get_successors():
            if successor not in closed_list:
                heapq.heappush(open_list, (successor.moves + heuristic(successor, goal_pos), successor))
                closed_list.add(successor)
                max_depth = max(max_depth, successor.moves)
    
    return None

def manhattan_heuristic(state, goal_pos):
    player_pos = state.car_positions['A'][0]
    return abs(player_pos[0] - goal_pos[0]) + abs(player_pos[1] - goal_pos[1])

def euclidean_heuristic(state, goal_pos):
    player_pos = state.car_positions['A'][0]
    return math.sqrt((player_pos[0] - goal_pos[0])**2 + (player_pos[1] - goal_pos[1])**2)

def misplaced_tiles_heuristic(state, goal_pos):
    player_pos = state.car_positions['A'][0]
    return 1 if player_pos != goal_pos else 0