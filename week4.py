import numpy as np
import math
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s^2)
T = 620000  # Thrust (N)
W = 229800  # Aircraft weight (N)
Uacc = 0.015  # Friction coefficient during acceleration
Udec = 0.40  # Friction coefficient during deceleration
CD = 0.0233  # Drag coefficient
CL = 0.15  # Lift coefficient
CLmax = 1.24  # Maximum lift coefficient
rho = 1.225  # Air density (kg/m^3)
S = 363.1  # Wing surface area (m^2)

# Compute velocities
Vmin = math.sqrt((2 * W) / (CLmax * rho * S))  # Stall speed (minimum velocity)
VOne = 249 / 3.6  # Convert 249 km/h to m/s (decision speed V1)
Vlof = 1.2 * VOne  # Lift-off velocity (1.2 times stall speed)

print(f"Stall speed Vmin: {Vmin:.2f} m/s")
print(f"Lift-off speed Vlof: {Vlof:.2f} m/s")

V1_range = np.linspace(VOne, Vlof, 100)  # Range of decision velocities

# Function to compute acceleration distance
def accel_distance(v1):
    p = g * ((T / W) - Uacc)  # Constant linear acceleration term
    q = (g * (CD - Uacc * CL) * S) / (2 * W)  # Quadratic drag term
    return (1 / (2 * q)) * np.log(1 + (q * v1**2) / p)  # Correct logarithmic formula

# Function to compute deceleration distance
def decel_distance(v1):
    a_decel = g * Udec  # Constant deceleration
    return v1**2 / (2 * a_decel)

# Compute total accelerate-stop distance
total_distance = [accel_distance(v1) + decel_distance(v1) for v1 in V1_range]

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(V1_range, total_distance, label='Runway Length vs Decision Velocity', color='b')
plt.xlabel('Decision Velocity V1 (m/s)')
plt.ylabel('Total Runway Length (m)')
plt.title('Accelerate-Stop Distance vs Decision Velocity (V1)')
plt.grid(True)
plt.legend()
plt.show()
