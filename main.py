from pathlib import Path
import os
from game import CarParkingPuzzle
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.ast import astar
from utils import measure_performance, write_output

def load_all_levels(levels_dir):
    levels = list(levels_dir.glob('*.txt'))
    return levels

def main():
    levels_dir = Path(r'C:\Users\guill\OneDrive\Documentos\CarParkingPuzzle\levels')  # Carpeta donde están los niveles
    levels = load_all_levels(levels_dir)
    algorithms = {'bfs': bfs, 'dfs': dfs, 'astar': astar}

    print("Seleccione un nivel:")
    for i, level_path in enumerate(levels):
        print(f"{i + 1}. Nivel {i + 1}")
    level_choice = int(input("Ingrese el número del nivel: ")) - 1
    level_file = levels[level_choice]

    print("Seleccione un algoritmo:")
    for i, algo in enumerate(algorithms.keys()):
        print(f"{i + 1}. {algo}")
    algo_choice = int(input("Ingrese el número del algoritmo: ")) - 1
    algo_name = list(algorithms.keys())[algo_choice]
    algorithm = algorithms[algo_name]

    puzzle = CarParkingPuzzle.load_level(level_file)

    # Mostrar el tablero inicial
    print("Tablero inicial:")
    puzzle.display_board()
    print()

    solve_with_performance = measure_performance(puzzle.solve)
    solution, time_taken, ram_usage = solve_with_performance(algorithm)

    if solution:
        print("Solución encontrada!")
        path_to_goal = []  # Generar secuencia de movimientos
        cost_of_path = len(solution)  # Número de movimientos
        nodes_expanded = len(solution)  # Número de nodos expandidos (asumiendo que se expanden todos los movimientos)
        search_depth = len(solution)  # Profundidad de la solución
        max_search_depth = len(solution)  # Máxima profundidad de búsqueda (en este caso, igual a la profundidad de la solución)
        
        # Ruta completa donde se generará output.txt
        output_file = r'C:\Users\guill\OneDrive\Documentos\CarParkingPuzzle\output.txt'
        
        # Guardar resultados en output.txt
        write_output(output_file, path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, time_taken, ram_usage)

    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    main()