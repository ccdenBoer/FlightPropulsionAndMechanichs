import numpy as np
import math
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import math

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
Vmin = math.sqrt((2 * W) / (CLmax * rho * S))  # Minimum velocity
VOne = 249 / 3.6
print(Vmin)
Vlof = 1.2 * VOne  # Lift-off velocity (m/s)
V1_range = np.linspace(VOne, Vlof, 100)  # Range of decision velocities (m/s)

# Function to compute acceleration distance
def accel_distance(v1):
    p = g * ((T / W) - Uacc)
    q = (g * ((CD - (Uacc * CL)) * S)) / (2 * W)
    
    return (1 / (2 * q)) * (np.log(p + (q * (v1**2)) / (np.log(p))))

# Function to compute deceleration distance
def decel_distance(v1):
    a_decel = g * Udec  # Deceleration
    return (v1**2) / (2 * a_decel)

# Compute total accelerate-stop distance
total_distance = [accel_distance(v1) + decel_distance(v1) for v1 in V1_range]
print(accel_distance(VOne))

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(V1_range, total_distance, label='Runway Length vs Decision Velocity', color='b')
plt.xlabel('Decision Velocity V1 (m/s)')
plt.ylabel('Total Runway Length (m)')
plt.title('Accelerate-Stop Distance vs Decision Velocity (V1)')
plt.grid(True)
plt.legend()
plt.show()
