def heuristic1(state, player_car='A', goal='0'):
    player_pos = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == player_car)
    goal_pos = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == goal)
    return abs(player_pos[0] - goal_pos[0]) + abs(player_pos[1] - goal_pos[1])

def heuristic2(state, player_car='A', goal='0'):
    player_pos = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == player_car)
    goal_pos = next((i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == goal)

    if player_pos[0] != goal_pos[0]:
        return float('inf')

    row = state[player_pos[0]]
    start, end = sorted([player_pos[1], goal_pos[1]])
    obstacles = sum(1 for cell in row[start:end] if cell not in (player_car, '.'))

    return obstacles

def heuristic3(state, player_car='A', goal='0'):
    h1 = heuristic1(state, player_car, goal)
    h2 = heuristic2(state, player_car, goal)
    return h1 + h2