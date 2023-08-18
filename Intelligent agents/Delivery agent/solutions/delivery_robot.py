# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:10:16 2023

@author: BarbaraS
"""

import random
import matplotlib.pyplot as plt

# Environment Setup
grid_size = 10
obstacles = [(3, 4), (5, 7), (8, 2)]
packages = [(1, 2), (4, 6), (7, 8)]
agent_pos = (0, 0)
time = 0

# Agent Initialization
path_taken = []
packages_delivered = []

# Simulation Loop
while packages:
    # Display Environment
    plt.clf()  # Clear previous plot
    for row in range(grid_size):
        for col in range(grid_size):
            if (row, col) in obstacles:
                plt.plot(col, row, "ks", markersize=10)
            else:
                plt.plot(col, row, "ko")
    
    # Display Delivered Packages
    for package in packages_delivered:
        plt.plot(package[1], package[0], "go", markersize=8)
    
    # Display Robot Path
    path_x = [pos[1] for pos in path_taken]
    path_y = [pos[0] for pos in path_taken]
    plt.plot(path_x, path_y, "b-")
    
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Time: {time}")
    plt.xlim(0, grid_size - 1)
    plt.ylim(0, grid_size - 1)
    plt.pause(0.5)  # Pause for visualization

    # Agent Behavior
    if packages:
        next_package = packages[0]
        if agent_pos == next_package:
            packages.pop(0)
            packages_delivered.append(next_package)
            path_taken.append(agent_pos)
    
    valid_moves = []
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = agent_pos[0] + move[0], agent_pos[1] + move[1]
        if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size and new_pos not in obstacles:
            valid_moves.append(new_pos)
            
        if len(path_taken)>2 and new_pos == path_taken[-2]:
           valid_moves.remove(new_pos)
    
    if valid_moves:
        
        agent_pos = random.choice(valid_moves)
        path_taken.append(agent_pos)
    
    time += 1

# Final Visualization
plt.clf()
for row in range(grid_size):
    for col in range(grid_size):
        if (row, col) in obstacles:
            plt.plot(col, row, "ks", markersize=10)
        else:
            plt.plot(col, row, "ko")
for package in packages_delivered:
    plt.plot(package[1], package[0], "go", markersize=8)
path_x = [pos[1] for pos in path_taken]
path_y = [pos[0] for pos in path_taken]
plt.plot(path_x, path_y, "b-")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Final Path")
plt.xlim(0, grid_size - 1)
plt.ylim(0, grid_size - 1)
plt.show()
