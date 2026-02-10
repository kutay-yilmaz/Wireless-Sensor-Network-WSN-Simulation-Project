"""
Wireless Sensor Network (WSN) - Step 4: Comparative Analysis
Author: Ismail Kutay Yilmaz
Description: This script compares the network lifetime of a Standard WSN (Battery-powered)
vs. a Solar Harvesting WSN (Hybrid).

- Red Line: Standard WSN (Dies quickly)
- Green Line: Solar WSN (Sustains operation)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# --- SETTINGS ---
FIELD_SIZE = 100
NUM_NODES = 100
BS_X, BS_Y = 50, 50
TOTAL_ROUNDS = 1500     
INITIAL_ENERGY = 0.5  

# --- SOLAR HARVESTING PARAMETER ---
# Energy gained per round during 'daytime'
SOLAR_CHARGE_RATE = 0.002 

class SensorNode:
    def __init__(self, id, has_solar):
        self.id = id
        self.solar = has_solar
        self.x = random.uniform(0, FIELD_SIZE)
        self.y = random.uniform(0, FIELD_SIZE)
        self.energy = INITIAL_ENERGY
        self.alive = True
        self.distance = np.sqrt((self.x - BS_X)**2 + (self.y - BS_Y)**2)

# --- SETUP TEAMS ---
# Team 1: Standard
nodes_standard = []
for i in range(NUM_NODES):
    nodes_standard.append(SensorNode(i, has_solar=False))

# Team 2: Solar (Cloned positions for fair comparison)
nodes_solar = []
for n in nodes_standard:
    new_node = SensorNode(n.id, has_solar=True)
    new_node.x = n.x
    new_node.y = n.y
    new_node.distance = n.distance
    nodes_solar.append(new_node)

# --- METRICS STORAGE ---
alive_count_std = []
alive_count_sol = []

print("Running comparative simulation...")

for r in range(TOTAL_ROUNDS):
    
    # Day/Night Cycle Logic (50 rounds cycle: 25 day / 25 night)
    is_daytime = (r % 50) < 25 

    # 1. SIMULATE STANDARD NODES
    alive_std = 0
    for node in nodes_standard:
        if node.alive:
            loss = 0.000001 * (node.distance ** 2)
            node.energy -= loss
            if node.energy <= 0:
                node.alive = False
            else:
                alive_std += 1
    alive_count_std.append(alive_std)

    # 2. SIMULATE SOLAR NODES
    alive_sol = 0
    for node in nodes_solar:
        if node.alive:
            loss = 0.000001 * (node.distance ** 2)
            node.energy -= loss
            
            # Harvesting Logic
            if is_daytime:
                node.energy += SOLAR_CHARGE_RATE
                if node.energy > INITIAL_ENERGY:
                    node.energy = INITIAL_ENERGY
            
            if node.energy <= 0:
                node.alive = False
            else:
                alive_sol += 1
    alive_count_sol.append(alive_sol)

# --- PLOTTING ---
plt.figure(figsize=(10, 6))

plt.plot(alive_count_std, color='red', linestyle='--', linewidth=2, label='Standard WSN (Battery)')
plt.plot(alive_count_sol, color='green', linewidth=3, label='Solar Harvesting WSN (Proposed)')

plt.title(f'Network Lifetime Comparison ({TOTAL_ROUNDS} Rounds)')
plt.xlabel('Time (Rounds)')
plt.ylabel('Number of Alive Nodes')
plt.grid(True, alpha=0.3)
plt.legend()

print("Comparison plot generated.")
plt.show()
