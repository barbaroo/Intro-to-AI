# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:43:29 2023

@author: BarbaraS
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:51:56 2023

@author: BarbaraS
"""

import random
import matplotlib.pyplot as plt

class Environment:
    def __init__(self, grid_size, obstacles, packages):
        # Your code for initializing the environment goes here
        
    def display(self, agent_pos, packages_delivered, path_taken, time):
        # Your code for displaying the environment goes here

class Agent:
    def __init__(self, agent_pos):
        # Your code for initializing the agent goes here
        
    def choose_valid_move(self, valid_moves):
        # Your code for choosing a valid move goes here
        
    def update_position(self, new_pos):
        # Your code for updating the agent's position goes here

class Simulation:
    def __init__(self, environment, agent):
        # Your code for initializing the simulation goes here
        
    def run(self):
        # Your code for running the simulation goes here

def main():
    grid_size = 10
    obstacles = [(3, 4), (5, 7), (8, 2)]
    packages = [(1, 2), (4, 6), (7, 8)]
    agent_pos = (0, 0)
    
    env = Environment(grid_size, obstacles, packages)
    agent = Agent(agent_pos)
    simulation = Simulation(env, agent)
    simulation.run()

if __name__ == "__main__":
    main()
