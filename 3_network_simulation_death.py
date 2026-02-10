"""
Wireless Sensor Network (WSN) - Step 3: Network Lifetime Simulation
Author: Ismail Kutay Yilmaz
Description: This script simulates the energy consumption of sensor nodes over time.
Nodes closer to the Base Station survive longer, while distant nodes deplete energy 
faster (Energy Hole Problem).

- Green Nodes: Alive
- Black Nodes: Dead (Energy Depleted)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# --- SIMULATION PARAMETERS ---
FIELD_SIZE = 100
NUM_NODES = 100
BS_X, BS_Y = 50, 50
TOTAL_ROUNDS = 1500        # Simulation duration
INITIAL_ENERGY = 0.5       # Joules

# --- SENSOR NODE CLASS ---
class SensorNode:
    def __init__(self, id):
        self.id = id
        self.x = random.uniform(0, FIELD_SIZE)
        self.y = random.uniform(0, FIELD_SIZE)
        self.energy = INITIAL_ENERGY
        self.alive = True
        # Calculate distance to Base Station
        self.distance = np.sqrt((self.x - BS_X)**2 + (self.y - BS_Y)**2)

# --- INITIALIZATION ---
nodes = []
for i in range(NUM_NODES):
    nodes.append(SensorNode(i))

print(f"Starting simulation for {TOTAL_ROUNDS} rounds...")

# --- MAIN SIMULATION LOOP ---
for r in range(TOTAL_ROUNDS):
    for node in nodes:
        if node.alive:
            # Energy Consumption Model: E_loss = k * distance^2
            loss = 0.000001 * (node.distance ** 2)
            node.energy -= loss
            
            if node.energy <= 0:
                node.alive = False
                node.energy = 0

# --- DATA COLLECTION FOR PLOTTING ---
x_alive, y_alive = [], []
x_dead, y_dead = [], []

for node in nodes:
    if node.alive:
        x_alive.append(node.x)
        y_alive.append(node.y)
    else:
        x_dead.append(node.x)
        y_dead.append(node.y)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 8))

# Plot Alive Nodes (Green)
plt.scatter(x_alive, y_alive, color='lime', s=100, edgecolors='black', label='Alive Nodes')

# Plot Dead Nodes (Black)
plt.scatter(x_dead, y_dead, color='black', s=100, edgecolors='black', label='Dead Nodes')

# Plot Base Station (Red X)
plt.scatter(BS_X, BS_Y, color='red', s=200, marker='X', label='Base Station', zorder=10)

plt.title(f'WSN Network Status after {TOTAL_ROUNDS} Rounds')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

print("Simulation complete. Generating plot...")
plt.show()
