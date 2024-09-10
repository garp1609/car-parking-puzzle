import os
from pathlib import Path
from game import CarParkingPuzzle
from utils import read_board, write_output, measure_performance
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar1 import astar1
from algorithms.astar2 import astar2
from algorithms.astar3 import astar3

def load_all_levels(levels_dir):
    levels = list(levels_dir.glob('*.txt'))
    return levels

def main():
    levels_dir = Path(r'C:\Users\guill\OneDrive\Documentos\CarParkingPuzzle\levels')  # Carpeta donde están los niveles
    levels = load_all_levels(levels_dir)
    algorithms = {'bfs': bfs, 'dfs': dfs, 'astar1': astar1, 'astar2': astar2, 'astar3': astar3}

    print("Seleccione un nivel:")
    for i, level in enumerate(levels):
        print(f"{i + 1}. {level}")
    level_choice = int(input("Ingrese el número del nivel: ")) - 1
    level_file = levels[level_choice]

    print("Seleccione un algoritmo:")
    for i, algo in enumerate(algorithms.keys()):
        print(f"{i + 1}. {algo}")
    algo_choice = int(input("Ingrese el número del algoritmo: ")) - 1
    algo_name = list(algorithms.keys())[algo_choice]
    algorithm = algorithms[algo_name]

    puzzle = CarParkingPuzzle.load_level(level_file)
    puzzle.display_board()

    solve_with_performance = measure_performance(puzzle.solve)
    solution, time_taken, ram_usage = solve_with_performance(algorithm)

    if solution:
        print("Solución encontrada!")
        path_to_goal = []  # Generar secuencia de movimientos
        cost_of_path = 0  # Número de movimientos
        nodes_expanded = 0  # Número de nodos expandidos
        search_depth = 0  # Profundidad de la solución
        max_search_depth = 0  # Máxima profundidad de búsqueda
        write_output('output.txt', path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, time_taken, ram_usage)
    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    main()