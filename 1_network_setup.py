"""
Wireless Sensor Network (WSN) - Step 1: Network Initialization
Author: Ismail Kutay Yilmaz
Description: This script simulates the random deployment of sensor nodes 
in a 2D field. It visualizes the initial topology of the network.
"""

import matplotlib.pyplot as plt
import random

# --- CONFIGURATION PARAMETERS ---
FIELD_SIZE = 100    # The area size is 100x100 meters
NUM_NODES = 50      # Total number of sensor nodes to deploy
BS_X, BS_Y = 50, 50 # Coordinates of the Base Station (Sink Node) - Placed at the center

# --- NODE DEPLOYMENT ---
# Lists to store the X and Y coordinates of the sensors
x_coords = []
y_coords = []

print(f"Deploying {NUM_NODES} sensor nodes randomly over a {FIELD_SIZE}x{FIELD_SIZE}m area...")

for i in range(NUM_NODES):
    # Generate random coordinates within the field boundaries
    x_val = random.uniform(0, FIELD_SIZE)
    y_val = random.uniform(0, FIELD_SIZE)
    
    x_coords.append(x_val)
    y_coords.append(y_val)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 8))

# 1. Plot Sensor Nodes
# We use blue dots to represent standard sensor nodes
plt.scatter(x_coords, y_coords, color='blue', s=100, edgecolors='black', label='Sensor Nodes')

# 2. Plot Base Station
# We use a large red 'X' to represent the Sink/Base Station at the center
plt.scatter(BS_X, BS_Y, color='red', s=200, marker='X', label='Base Station (Sink)', zorder=10)

# 3. Graph Settings
plt.title('Wireless Sensor Network (WSN) - Random Topology Distribution')
plt.xlabel('X Coordinate (meters)')
plt.ylabel('Y Coordinate (meters)')
plt.legend(loc='upper right') # Show legend to identify nodes vs base station
plt.grid(True, linestyle='--', alpha=0.6) # Add grid for better readability
plt.tight_layout()

# Show the final plot
print("Topology visualization generated successfully.")
plt.show()
