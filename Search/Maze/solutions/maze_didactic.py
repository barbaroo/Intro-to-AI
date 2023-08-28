# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:09:53 2023

@author: BarbaraS
"""

import sys

def create_node(state, parent, action):
    return {
        "state": state,
        "parent": parent,
        "action": action
    }

def create_stack_frontier():
    return []

def add_to_frontier(frontier, node):
    frontier.append(node)

def contains_state(frontier, state):
    return any(node["state"] == state for node in frontier)

def frontier_is_empty(frontier):
    return len(frontier) == 0

def remove_from_stack_frontier(frontier):
    if frontier_is_empty(frontier):
        raise Exception("empty frontier")
    else:
        node = frontier[-1]
        frontier.pop()
        return node

def remove_from_queue_frontier(frontier):
    if frontier_is_empty(frontier):
        raise Exception("empty frontier")
    else:
        node = frontier[0]
        frontier.pop(0)
        return node

def load_maze(filename):
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
    num_explored = 0
    start_node = create_node(state=start, parent=None, action=None)
    frontier = create_stack_frontier()
    add_to_frontier(frontier, start_node)
    explored = set()

    while True:
        if frontier_is_empty(frontier):
            raise Exception("no solution")

        node = remove_from_stack_frontier(frontier)
        num_explored += 1

        if node["state"] == goal:
            actions = []
            cells = []
            while node["parent"] is not None:
                actions.append(node["action"])
                cells.append(node["state"])
                node = node["parent"]
            actions.reverse()
            cells.reverse()
            solution = (actions, cells)
            return solution, num_explored, explored

        explored.add(node["state"])

        for action, state in neighbors(walls, height, width, node["state"]):
            if not contains_state(frontier, state) and state not in explored:
                child = create_node(state=state, parent=node, action=action)
                add_to_frontier(frontier, child)

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