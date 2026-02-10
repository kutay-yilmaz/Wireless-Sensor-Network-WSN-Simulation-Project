"""
Wireless Sensor Network (WSN) - Step 2: Energy & Distance Analysis
Author: Ismail Kutay Yilmaz
Description: This script calculates the Euclidean distance of each sensor node 
from the Base Station (Sink). It visualizes the network using a color gradient 
to represent distance, which is directly correlated with energy consumption 
(Path Loss Model).

- Green Nodes: Close to BS (Low Energy Consumption)
- Red Nodes: Far from BS (High Energy Consumption)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# --- CONFIGURATION PARAMETERS ---
FIELD_SIZE = 100    # 100x100 meters area
NUM_NODES = 50      # Number of nodes
BS_X, BS_Y = 50, 50 # Base Station coordinates (Center)

# --- DATA GENERATION ---
x_coords = []
y_coords = []
distances = []

print("Calculating distances for energy analysis...")

for i in range(NUM_NODES):
    # Random Position
    x_val = random.uniform(0, FIELD_SIZE)
    y_val = random.uniform(0, FIELD_SIZE)
    
    # Calculate Euclidean Distance to Base Station
    # Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    dist = np.sqrt((x_val - BS_X)**2 + (y_val - BS_Y)**2)
    
    x_coords.append(x_val)
    y_coords.append(y_val)
    distances.append(dist)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 8))

# 1. Plot Sensor Nodes with Color Map
# 'c=distances': Color is determined by distance
# 'cmap=RdYlGn_r': Red-Yellow-Green (Reverse). Far=Red, Close=Green.
sc = plt.scatter(x_coords, y_coords, c=distances, cmap='RdYlGn_r', s=100, edgecolors='black', label='Sensor Nodes')

# 2. Plot Base Station
plt.scatter(BS_X, BS_Y, c='red', s=200, marker='X', label='Base Station (Sink)', zorder=10)

# 3. Add Color Bar (Legend for Distance)
cbar = plt.colorbar(sc)
cbar.set_label('Distance to Base Station (m)')

# 4. Graph Settings
plt.title('WSN Energy Distribution Map (Distance Analysis)')
plt.xlabel('X Coordinate (m)')
plt.ylabel('Y Coordinate (m)')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show Result
print("Energy map generated successfully.")
plt.show()
