# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:51:56 2023

@author: BarbaraS
"""

import random
import matplotlib.pyplot as plt

class Environment:
    def __init__(self, grid_size, obstacles, packages):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.packages = packages
    
    def display(self, agent_pos, packages_delivered, path_taken, time):
        #plt.clf()  # Clear previous plot
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if (row, col) in self.obstacles:
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
        plt.title(f"Time: {time}")
        plt.xlim(0, self.grid_size - 1)
        plt.ylim(0, self.grid_size - 1)
        plt.pause(0.5)  # Pause for visualization
        plt.show()

class Agent:
    def __init__(self, agent_pos):
        self.agent_pos = agent_pos
        self.path_taken = []
    
    def choose_valid_move(self, valid_moves):
        return random.choice(valid_moves)
    
    def update_position(self, new_pos):
        self.agent_pos = new_pos
        self.path_taken.append(new_pos)

class Simulation:
    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent
        self.time = 0
    
    def run(self):
        packages_delivered = []
        
        while self.environment.packages:
            self.environment.display(self.agent.agent_pos, packages_delivered, self.agent.path_taken, self.time)
            
            if self.environment.packages:
                next_package = self.environment.packages[0]
                if self.agent.agent_pos == next_package:
                    self.environment.packages.pop(0)
                    packages_delivered.append(next_package)
                    self.agent.path_taken.append(self.agent.agent_pos)
            
            valid_moves = []
            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_pos = self.agent.agent_pos[0] + move[0], self.agent.agent_pos[1] + move[1]
                if (
                    0 <= new_pos[0] < self.environment.grid_size
                    and 0 <= new_pos[1] < self.environment.grid_size
                    and new_pos not in self.environment.obstacles
                ):
                    valid_moves.append(new_pos)
                
                if len(self.agent.path_taken) > 2 and new_pos == self.agent.path_taken[-2]:
                    valid_moves.remove(new_pos)
            
            if valid_moves:
                new_pos = self.agent.choose_valid_move(valid_moves)
                self.agent.update_position(new_pos)
            
            self.time += 1
        
        self.environment.display(self.agent.agent_pos, packages_delivered, self.agent.path_taken, "Final Path")

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
