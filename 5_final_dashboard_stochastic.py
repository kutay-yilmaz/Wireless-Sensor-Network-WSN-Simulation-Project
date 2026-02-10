"""
Wireless Sensor Network (WSN) - Step 5: Final Dashboard & Stochastic Analysis
Author: Ismail Kutay Yilmaz
Description: This advanced simulation includes a Stochastic Weather Model 
(Random Sunny/Cloudy/Rainy days) and analyzes both Network Lifetime and 
Total Data Throughput.

Key Features:
- Stochastic Weather Modeling (Randomized Energy Harvesting)
- Throughput Analysis (Total Packets Delivered)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# --- SYSTEM CONFIGURATION ---
FIELD_SIZE = 100
NUM_NODES = 100
BS_X, BS_Y = 50, 50
TOTAL_ROUNDS = 2000     
INITIAL_ENERGY = 0.5  
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

# --- SETUP ---
nodes_standard = [SensorNode(i, has_solar=False) for i in range(NUM_NODES)]
nodes_solar = []
for n in nodes_standard:
    new_node = SensorNode(n.id, has_solar=True)
    new_node.x, new_node.y, new_node.distance = n.x, n.y, n.distance
    nodes_solar.append(new_node)

# --- METRICS ---
history_alive_std = []
history_alive_sol = []
history_packets_std = []
history_packets_sol = []

total_packets_std = 0
total_packets_sol = 0

print("Starting Stochastic Simulation...")

for r in range(TOTAL_ROUNDS):
    
    # --- STOCHASTIC WEATHER MODEL ---
    # Simulating real-world weather variability
    weather_luck = random.random()
    current_charge = 0
    
    if weather_luck < 0.6:
        current_charge = SOLAR_CHARGE_RATE       # Sunny (Full Charge)
    elif weather_luck < 0.9:
        current_charge = SOLAR_CHARGE_RATE * 0.5 # Cloudy (Half Charge)
    else:
        current_charge = 0                       # Rainy (No Charge)

    # 1. STANDARD WSN LOOP
    alive_count = 0
    for node in nodes_standard:
        if node.alive:
            loss = 0.000001 * (node.distance ** 2)
            node.energy -= loss
            if node.energy <= 0:
                node.alive = False
            else:
                alive_count += 1
                total_packets_std += 1
    history_alive_std.append(alive_count)
    history_packets_std.append(total_packets_std)

    # 2. SOLAR WSN LOOP
    alive_count = 0
    for node in nodes_solar:
        if node.alive:
            loss = 0.000001 * (node.distance ** 2)
            node.energy -= loss
            
            # Apply Stochastic Charging
            if node.solar:
                node.energy += current_charge
                if node.energy > INITIAL_ENERGY:
                    node.energy = INITIAL_ENERGY
            
            if node.energy <= 0:
                node.alive = False
            else:
                alive_count += 1
                total_packets_sol += 1

    history_alive_sol.append(alive_count)
    history_packets_sol.append(total_packets_sol)

# --- DASHBOARD VISUALIZATION ---
plt.figure(figsize=(10, 10))

# Plot 1: Alive Nodes
plt.subplot(2, 1, 1)
plt.plot(history_alive_std, color='red', linestyle='--', label='Standard WSN')
plt.plot(history_alive_sol, color='green', linewidth=2, label='Solar WSN')
plt.title('Network Lifetime (Alive Nodes)')
plt.ylabel('Node Count')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Total Packets (Throughput)
plt.subplot(2, 1, 2)
plt.plot(history_packets_std, color='red', linestyle='--', label='Standard Throughput')
plt.plot(history_packets_sol, color='green', linewidth=2, label='Solar Throughput')
plt.title('Total Data Packets Delivered')
plt.xlabel('Simulation Rounds')
plt.ylabel('Total Packets')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
print("Dashboard generated.")
plt.show()
