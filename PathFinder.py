import pathfinding
import random
import re
from colorama import init
from termcolor import colored
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.best_first import BestFirst
from pathfinding.finder.bi_a_star import BiAStarFinder
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.ida_star import IDAStarFinder
from pathfinding.finder.msp import MinimumSpanningTree

def user_trash():

    print("\n[ESMA©]****************Pathfinder****************[ESMA©]\n")
    try:
        user_input = input("Input height and width of the graph: ")
        the_input = user_input.split(" ")
        if len(the_input) == 2 and re.match("[0-9]", the_input[0]) and re.match("[0-9]", the_input[1]):
            return the_input
        else:
            return None
    except:
        return None

def movement_input():
    try:
        allow_diag = input("\nAllow diagonal movement? (y/n) (default: y): ")
        if len(allow_diag) == 1 and re.match("[yYnN]", allow_diag):
            if allow_diag == "y":
                return DiagonalMovement.always
            else: 
                return DiagonalMovement.never
        else: 
            return None
    except:
        return None

def map_maker(matrix, height, width):

    for row in range(height):
        matrix.append([random.randrange(0, 8) for x in range(width)])
    return matrix

def pathfinder(matrix, pathfindingfunction, diag_movement):

    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(grid.width-1, grid.height-1)

    finder = pathfindingfunction(diagonal_movement=diag_movement)
    path, runs = finder.find_path(start, end, grid)

    print('\n|'+ algorithm_string(pathfindingfunction) +'| operations:', runs, '| path length:', len(path),'|')
    print(grid.grid_str(path=path, start=start, end=end, start_chr=colored('S', 'blue'), end_chr=colored('E', 'magenta'), path_chr=colored('x', 'green')))

def algorithm_string(pathfindingfunction):
    if pathfindingfunction is AStarFinder:
        return "A* search algorithm"
    elif pathfindingfunction is BestFirst:
        return "Best First algoritm"
    elif pathfindingfunction is BiAStarFinder:
        return "Bidirectional search algoritm"
    elif pathfindingfunction is BreadthFirstFinder:
        return "Breadth First Search"
    elif pathfindingfunction is DijkstraFinder:
        return "Dijkstra's algorithm"
    elif pathfindingfunction is IDAStarFinder:
        return "Iterative deepening A*"
    elif pathfindingfunction is MinimumSpanningTree:
        return "Minimum spanning tree"

if __name__ == '__main__':
    
    init()
    function_list = [AStarFinder, BestFirst, BiAStarFinder, BreadthFirstFinder, DijkstraFinder, MinimumSpanningTree]
    matrix = []
    size_input = user_trash()
    diag_movement = movement_input()

    if size_input is None or diag_movement is None:
        print("Incorret input!")

    else:
        map_maker(matrix, (int(size_input[0])), (int(size_input[1])))
        
        print(colored('\nS', 'blue') + " = start\n" + colored('E', 'magenta') + " = end\n# = obstacle\n" + colored('x', 'green') + " = path")
        for function in function_list:
            pathfinder(matrix, function, diag_movement)

    exit_input = input('Press enter key to exit')
    if exit_input:
        exit(0)

#To-do: Tilføje muligheden for selv at vælge start og slut punkt.
