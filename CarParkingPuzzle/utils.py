import time
import psutil
import os

def read_board(file_path):
    with open(file_path, 'r') as file:
        board = [list(line.strip()) for line in file.readlines()]
    return board

def write_output(file_path, path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, running_time, max_ram_usage):
    with open(file_path, 'w') as file:
        file.write(f"path_to_goal: {path_to_goal}\n")
        file.write(f"cost_of_path: {cost_of_path}\n")
        file.write(f"nodes_expanded: {nodes_expanded}\n")
        file.write(f"search_depth: {search_depth}\n")
        file.write(f"max_search_depth: {max_search_depth}\n")
        file.write(f"running_time: {running_time}\n")
        file.write(f"max_ram_usage: {max_ram_usage}\n")

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process(os.getpid())
        result = func(*args, **kwargs)
        end_time = time.time()
        ram_usage = process.memory_info().rss / (1024 ** 2)  # Convert to MB
        return result, end_time - start_time, ram_usage
    return wrapper