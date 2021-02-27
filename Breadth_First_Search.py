import queue
import random


def createMaze(height, length):
    symbol_list = [" ", " ", " ", " "]
    maze = []

    for row in range(height):
        maze.append([random.choice(symbol_list) for x in range(length)])

    for colon in range(height):
        maze[colon][0] = "#"
        maze[colon][length-1] = "#"

    maze[0] = ["#" for x in range(length)]
    maze[length-1] = ["#" for x in range(length)]

    maze[0][random.randrange(1, length-1)] = "A"
    maze[height-1][random.randrange(1, length-1)] = "B"
    
    #old maze
    #maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    #maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    #maze.append(["#", " ", "#", "#", "#", "#", "#", " ", "#"])
    #maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    #maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    #maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    #maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    #maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    #maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                if j == len(maze)-1:
                    print("B ", end="")
                else:    
                    print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "A":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "B":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False


def no_path_found():
    for v in maze:
        print(v)
    print("No Path!")

# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze(10,10)
not_valid_move = 0
attempts = 0

for row in maze:
    for col in row:   
        print(col + " ", end="")
    print()

while not findEnd(maze, add):
    add = nums.get()
    attempts+=1
    print("Steps: ", add + " Attempts", attempts, end='\r')
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            not_valid_move = 0
            nums.put(put)
