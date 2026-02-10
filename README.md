# Solar Energy Harvesting Wireless Sensor Network (WSN) Simulation

## Project Overview
This project simulates the energy consumption and network lifetime of a Wireless Sensor Network (WSN). It specifically addresses the "Energy Hole Problem" inherent in standard battery-powered networks and proposes a Solar Energy Harvesting (Hybrid) solution to extend network longevity.

The simulation models real-world physical constraints, including Free Space Path Loss, stochastic weather conditions (Sunny/Cloudy/Rainy), and data throughput analysis to demonstrate the efficiency of the proposed system.

## Repository Structure

This project consists of 5 progressive steps, analyzing the network from initial deployment to final optimization:

| File Name | Description | Output |
| :--- | :--- | :--- |
| **1_network_setup.py** | **Step 1: Network Deployment.** Randomly distributes sensor nodes in a 100x100m field. Visualizes the initial topology. | Figure_1_Random_Distribution.png |
| **2_energy_map_analysis.py** | **Step 2: Distance & Energy Analysis.** Calculates Euclidean distance from the Sink Node. Generates a heat map showing high-risk (high energy consumption) zones. | Figure_2_Energy_Distance_Map.png |
| **3_network_simulation_death.py** | **Step 3: The Energy Hole Problem.** Simulates network operation until nodes deplete their batteries. Demonstrates that nodes far from the sink die first. | Figure_3_Network_Status_Dead_Alive.png |
| **4_comparative_analysis.py** | **Step 4: Standard vs. Solar.** Compares the lifetime of a standard battery-powered network against the proposed Solar Harvesting network. | Figure_4_Lifetime_Comparison.png |
| **5_final_dashboard_stochastic.py** | **Step 5: Final Dashboard.** The advanced simulation including a Stochastic Weather Model and Data Throughput Analysis. Compares total packets delivered. | Figure_5_Final_Dashboard.png |

## Key Features
* **Physics-Based Energy Model:** Energy consumption is modeled based on distance squared (E ~ d^2).
* **Stochastic Weather Modeling:** Simulates realistic weather variability (Sunny 60%, Cloudy 30%, Rainy 10%) for energy harvesting.
* **Comparative Analysis:** Direct comparison between Battery-only and Hybrid Solar nodes.
* **Throughput Analysis:** Tracks not just network lifetime, but total data packets successfully delivered to the Base Station.

## Results & Findings
1.  **Standard Networks:** Nodes far from the Base Station deplete energy rapidly, causing network partitioning around 300-400 rounds.
2.  **Solar Harvesting:** The proposed solution extends the network lifetime significantly. Even with variable weather, 60% of nodes remain active after 1500 rounds.
3.  **Efficiency:** The Solar Harvesting WSN delivers approximately 3x more data packets than the standard network.

## Author
**Ismail Kutay Yilmaz**
Electrical & Electronics Engineering
Toros University, Mersin
