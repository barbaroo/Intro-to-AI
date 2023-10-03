#Helper functions for maze solving algorithm



def load_maze(filename):
    """
    Load a maze from a file and return its representation, start, and goal positions.
    
    The maze is represented as a list of lists where each cell can be:
    - "A" representing the start position.
    - "B" representing the goal position.
    - " " representing an open space.
    - Any other character representing a wall.
    
    Args:
    - filename (str): The path to the file containing the maze.
    
    Returns:
    - walls (list of lists): A boolean matrix representing the maze. True for walls, False otherwise.
    - start (tuple): The coordinates of the start position.
    - goal (tuple): The coordinates of the goal position.
    """
    
    with open(filename) as f:
        contents = f.read()

    # Ensure there is only one start and one goal in the maze
    if contents.count("A") != 1:
        raise Exception("maze must have exactly one start point")
    if contents.count("B") != 1:
        raise Exception("maze must have exactly one goal")

    # Split the content by lines
    contents = contents.splitlines()
    height = len(contents)
    width = max(len(line) for line in contents)

    walls = []
    for i in range(height):
        row = []
        for j in range(width):
            try:
                if contents[i][j] == "A":
                    start = (i, j)
                    row.append(False)
                elif contents[i][j] == "B":
                    goal = (i, j)
                    row.append(False)
                elif contents[i][j] == " ":
                    row.append(False)
                else:
                    row.append(True)
            except IndexError:
                row.append(False)
        walls.append(row)

    return walls, start, goal

def print_maze(walls, start, goal, solution_path=None):
    """
    Print a visual representation of the maze with an optional solution path.
    
    Args:
    - walls (list of lists): A boolean matrix representing the maze. True for walls, False otherwise.
    - start (tuple): The coordinates of the start position.
    - goal (tuple): The coordinates of the goal position.
    - solution_path (list, optional): A list of tuples representing the coordinates of the solution path.
    """
    
    print()
    for i, row in enumerate(walls):
        for j, col in enumerate(row):
            if col:
                print("█", end="")
            elif (i, j) == start:
                print("A", end="")
            elif (i, j) == goal:
                print("B", end="")
            elif solution_path is not None and (i, j) in solution_path:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()

def neighbors_of_state(walls, state):
    """
    Determine the possible neighbors (moves) for a given state in the maze.
    
    Args:
    - walls (list of lists): A boolean matrix representing the maze. True for walls, False otherwise.
    - state (tuple): The current coordinates.
    
    Returns:
    - result (list): A list of tuples, where each tuple contains a move action (e.g., "up") and the resulting state coordinates.
    """
    
    row, col = state
    height = len(walls)
    width = len(walls[0])
    # Define potential move actions and their resulting states
    candidates = [
        ("up", (row - 1, col)),
        ("down", (row + 1, col)),
        ("left", (row, col - 1)),
        ("right", (row, col + 1))
    ]

    result = []
    for action, (r, c) in candidates:
        # Ensure the move is within the maze boundaries and not into a wall
        if 0 <= r < height and 0 <= c < width and not walls[r][c]:
            result.append((action, (r, c)))
    return result
