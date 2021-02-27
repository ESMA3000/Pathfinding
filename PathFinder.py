import pathfinding
import random
import re
from colorama import init
from termcolor import colored
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def user_trash():

    print("\n[ESMA©]****************Pathfinder****************[ESMA©]\n")

    try:
        user_input = input("Input height and width of the graph: ")
        if re.match("[0-9]", user_input):

            the_input = user_input.split(" ")
            if len(the_input) is 2 and re.match("[0-9]", the_input[0]) and re.match("[0-9]", the_input[1]):

                allow_diag = input("\nAllow diagonal movement? (y/n) (default: y): ")
                if allow_diag is "n":
                    diag_movement = None

                return the_input

            else:
                return None

        else:
            return None

    except:
        return None

def map_maker(matrix, height, width):

    for row in range(height):
        matrix.append([random.randrange(0, 10) for x in range(width)])

    return matrix

def pathfinder(matrix, diag_movement):

    grid = Grid(matrix=matrix)

    start = grid.node(0, 0)
    end = grid.node(grid.width-1, grid.height-1)

    finder = AStarFinder(diagonal_movement=diag_movement)
    path, runs = finder.find_path(start, end, grid)

    print(colored('S', 'blue') + " = start\n" + colored('E', 'magenta') + " = end\n# = obstacle\n" + colored('x', 'green') + " = path")
    print('\noperations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end, start_chr=colored('S', 'blue'), end_chr=colored('E', 'magenta'), path_chr=colored('x', 'green')))

init()
diag_movement = DiagonalMovement.always
matrix = []
size_input = user_trash()

if size_input is None:
    print("Incorret input!")

else: pathfinder(map_maker(matrix, (int(size_input[0])), (int(size_input[1]))), diag_movement)

exit_input = input('Press enter key to exit')
if exit_input:
    exit(0)

#To-do: Tilføje muligheden for selv at vælge start og slut punkt.
