# ☀️ Solar Energy Harvesting Wireless Sensor Network (WSN) Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)

## 📌 Project Overview
This project simulates the energy consumption and network lifetime of a **Wireless Sensor Network (WSN)**. It addresses the **"Energy Hole Problem"** in standard battery-powered networks and proposes a **Solar Energy Harvesting (Hybrid)** solution to extend network longevity.

The simulation models real-world physical constraints, including **Free Space Path Loss ($d^2$)**, stochastic weather conditions (Sunny/Cloudy/Rainy), and data throughput analysis.

## 📂 Repository Structure

This project consists of 5 progressive steps, analyzing the network from deployment to final optimization:

| File Name | Description | Output |
| :--- | :--- | :--- |
| **`1_network_setup.py`** | **Step 1: Network Deployment.** Randomly distributes 50-100 sensor nodes in a $100 \times 100m$ field. Visualizes the initial topology. | *Figure_1_Random_Distribution.png* |
| **`2_energy_map_analysis.py`** | **Step 2: Distance & Energy Analysis.** Calculates Euclidean distance from the Sink Node. Generates a heat map showing high-risk (high energy consumption) zones. | *Figure_2_Energy_Distance_Map.png* |
| **`3_network_simulation_death.py`** | **Step 3: The Energy Hole Problem.** Simulates network operation until nodes deplete their batteries. Demonstrates that nodes far from the sink die first. | *Figure_3_Network_Status_Dead_Alive.png* |
| **`4_comparative_analysis.py`** | **Step 4: Standard vs. Solar.** Compares the lifetime of a standard battery-powered network against the proposed Solar Harvesting network. | *Figure_4_Lifetime_Comparison.png* |
| **`5_final_dashboard_stochastic.py`** | **Step 5: Final Dashboard.** The advanced simulation including a **Stochastic Weather Model** and **Data Throughput Analysis**. Compares total packets delivered. | *Figure_5_Final_Dashboard.png* |

## 🚀 Key Features
* **Physics-Based Energy Model:** Energy consumption is modeled based on distance ($E \propto d^2$).
* **Stochastic Weather Modeling:** Simulates realistic weather variability (Sunny 60%, Cloudy 30%, Rainy 10%) for energy harvesting.
* **Comparative Analysis:** Direct comparison between Battery-only and Hybrid Solar nodes.
* **Throughput Analysis:** Tracks not just network lifetime, but total data packets successfully delivered to the Base Station.

## 📊 Results & Findings
1.  **Standard Networks:** Nodes far from the Base Station deplete energy rapidly, causing an "Energy Hole" and network partitioning around **300-400 rounds**.
2.  **Solar Harvesting:** The proposed solution extends the network lifetime significantly. Even with variable weather, **60% of nodes remain active** after 1500 rounds.
3.  **Efficiency:** The Solar Harvesting WSN delivers approximately **3x more data packets** than the standard network.

## 🛠️ Installation & Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/Solar-Harvesting-WSN-Simulation.git](https://github.com/yourusername/Solar-Harvesting-WSN-Simulation.git)
    ```
2.  Install dependencies:
    ```bash
    pip install matplotlib numpy
    ```
3.  Run the simulations:
    ```bash
    python 5_final_dashboard_stochastic.py
    ```

## 👨‍💻 Author
**Ismail Kutay Yilmaz**
*Electrical & Electronics Engineering*
*Toros University, Mersin*

---
*This project was developed as a comprehensive analysis of energy efficiency in WSNs.*
