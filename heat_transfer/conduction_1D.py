import numpy as np
import matplotlib.pyplot as plt

# Defining the problem parameters
L = 50.0  # Length of rod (mm)
a = 110  # Thermal diffusivity
time = 4.0  # Time (s)
node = 10  # Number of nodes

dx = L / (node - 1)  # Spatial step size
dt = (0.5 * dx**2) / a  # Time step size

# Initialization
T = np.zeros(node) + 20  # Temperature array initialized to 20°C
T[0] = 100  # Boundary condition at x=0
T[-1] = 100  # Boundary condition at x=L


# Time-stepping loop
counter = 0.0
while counter < time:
    Tn = T.copy()  # Copy of the current temperature distribution
    for i in range(1, node - 1):
        T[i] = Tn[i] + a * dt / dx**2 * (Tn[i + 1] - 2 * Tn[i] + Tn[i - 1])
    counter += dt
    print(f"Time: {counter:.2f} s, Average Temperature: {np.average(T)}°C")
    