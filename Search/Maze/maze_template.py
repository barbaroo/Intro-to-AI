# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:16:18 2023

@author: BarbaraS
"""

import sys

# TODO: Implement the node data structure
# A node should have three properties:
# 1. state - The current state or position of the node
# 2. parent - The parent node that led to this node
# 3. action - The action taken to move to this state from the parent
def create_node(state, parent, action):
    pass

# TODO: Implement the stack frontier
# The frontier should be able to:
# 1. Add nodes to the frontier
# 2. Check if a state exists in the frontier
# 3. Check if the frontier is empty
# 4. Remove nodes from the frontier

def create_stack_frontier():
    pass

def add_to_frontier(frontier, node):
    pass

def contains_state(frontier, state):
    pass

def frontier_is_empty(frontier):
    pass

def remove_from_stack_frontier(frontier):
    pass

def remove_from_queue_frontier(frontier):
    pass

def load_maze(filename):
    # Read the maze from a file and return its structure, start, and end positions
    with open(filename) as f:
        contents = f.read()

    if contents.count("A") != 1:
        raise Exception("maze must have exactly one start point")
    if contents.count("B") != 1:
        raise Exception("maze must have exactly one goal")

    contents = contents.splitlines()
    height = len(contents)
    width = max(len(line) for line in contents)
    walls = []
    start = None
    goal = None

    for i in range(height):
        row = []
        for j in range(width):
            if j < len(contents[i]) and contents[i][j] == "A":
                start = (i, j)
                row.append(False)
            elif j < len(contents[i]) and contents[i][j] == "B":
                goal = (i, j)
                row.append(False)
            elif j < len(contents[i]) and contents[i][j] == " ":
                row.append(False)
            else:
                row.append(True)
        walls.append(row)

    return walls, start, goal

def print_maze(walls, start, goal, solution=None):
    # Print the maze structure to the console
    for i, row in enumerate(walls):
        for j, col in enumerate(row):
            if col:
                print("█", end="")
            elif (i, j) == start:
                print("A", end="")
            elif (i, j) == goal:
                print("B", end="")
            elif solution and (i, j) in solution[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()

def neighbors(walls, height, width, state):
    # Return the neighboring states of the given state that aren't walls
    row, col = state
    candidates = [
        ("up", (row - 1, col)),
        ("down", (row + 1, col)),
        ("left", (row, col - 1)),
        ("right", (row, col + 1))
    ]

    result = []
    for action, (r, c) in candidates:
        if 0 <= r < height and 0 <= c < width and not walls[r][c]:
            result.append((action, (r, c)))
    return result

def solve_maze(walls, start, goal, height, width):
    # TODO: Implement the maze-solving algorithm using the frontier
    # 1. Initialize the frontier with the start state
    # 2. Use a loop to keep exploring until the goal is found or the frontier is empty
    # 3. In each loop iteration, get a state from the frontier and explore its neighbors
    # 4. If a neighbor hasn't been explored and isn't in the frontier, add it to the frontier
    # 5. If the goal state is found, backtrack using the parent property of nodes to find the solution path

    pass

def main(filename):
    walls, start, goal = load_maze(filename)
    height = len(walls)
    width = len(walls[0])

    print("Maze:")
    print_maze(walls, start, goal)

    print("Solving...")
    solution, num_explored, explored = solve_maze(walls, start, goal, height, width)

    print("States Explored:", num_explored)
    print("Solution:")
    print_maze(walls, start, goal, solution)

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

main(sys.argv[1])
