# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:14:20 2023

@author: BarbaraS
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:10:16 2023

@author: BarbaraS
"""

import random
import matplotlib.pyplot as plt

def display_environment(grid_size, obstacles, packages_delivered, path_taken, agent_pos, time):
    # Your code for displaying the environment goes here

def main():
    grid_size = 10
    obstacles = [(3, 4), (5, 7), (8, 2)]
    packages = [(1, 2), (4, 6), (7, 8)]
    agent_pos = (0, 0)
    time = 0

    path_taken = []
    packages_delivered = []

    while packages:
        display_environment(grid_size, obstacles, packages_delivered, path_taken, agent_pos, time)
        
        # Your code for checking and delivering packages goes here
        
        valid_moves = []
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = agent_pos[0] + move[0], agent_pos[1] + move[1]
            if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size and new_pos not in obstacles:
                valid_moves.append(new_pos)

            # Your code for handling path constraints goes here

        if valid_moves:
            agent_pos = random.choice(valid_moves)
            path_taken.append(agent_pos)

        time += 1

    # Your code for final visualization goes here

if __name__ == "__main__":
    main()
