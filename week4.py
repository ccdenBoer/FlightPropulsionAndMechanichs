import numpy as np
import math
import matplotlib.pyplot as plt

# Constants and variables
g = 9.81  # gravitational acceleration (m/s^2)
rho = 1.225  # air density (kg/m^3)

# Aircraft parameters
T = 620000  # thrust (N)
Mass = 217000  # weight (Kg)
W = Mass * g  # weight (N)
mu = 0.015  # coefficient of friction
CD = 0.0233  # drag coefficient
CL = 0.15  # lift coefficient (for takeoff)
S = 122.6  # wing area (m^2)
V_LOF = 70.0  # lift-off velocity (m/s)

# Function to calculate the ground roll distance
def calculate_ground_run(v1):
    p = g * ((T / W) - mu)
    q = -(g * (CD - mu * CL) * rho * S) / (2 * W)

    ln_term = math.log(p + q * v1**2) - math.log(p)
    ground_roll_distance = (1 / (2 * q)) * ln_term
    print(ground_roll_distance)
    return ground_roll_distance

def calculate_transition_phase(v1):
    # Calculate lift and drag
    L = CL * rho * ((v1**2) / 2) * S
    D = CD * rho * ((v1**2) / 2) * S

    # Calculate the radius of the circular arc
    R = (W * v1**2) / (g * (L - W))
    
    # Calculate sin(γ)
    sin_gamma = (T - D) / W
    sin_gamma = max(-1, min(1, sin_gamma))  # Clamp sin_gamma to [-1, 1]

    # Ensure the angle γ is calculated in radians
    gamma = math.asin(sin_gamma)

    # Calculate h_b (vertical height)
    h_b = R * (1 - math.cos(gamma))

    # Calculate s_b (distance along the arc)
    s_b = R * gamma

    return s_b

# Function to calculate accelerate-stop distance
def calculate_accelerate_stop(v1):
    stopping_distance = v1**2 / (2 * g * mu)
    return stopping_distance

# Function to calculate the total runway length for AEO/OEI scenarios
def calculate_takeoff_length(v1):
    ground_run = calculate_ground_run(v1)
    transition = calculate_transition_phase(v1)
    total_runway_length = ground_run + transition
    return total_runway_length

# Function to calculate the landing runway length
def calculate_landing_length(v):
    flare_distance = 100  # Assuming a fixed flare distance
    ground_run = v**2 / (2 * g * mu)
    total_landing_length = flare_distance + ground_run
    return total_landing_length

def graph():
    v1_range = np.linspace(40, 80, 50)  # Range of decision velocities (m/s)

    # Initialize lists to store results
    ground_run_distances = []
    transition_distances = []
    total_takeoff_lengths = []
    accelerate_stop_distances = []
    landing_lengths = []

    # Loop through each velocity in the range
    for v1 in v1_range:
        ground_run = calculate_ground_run(v1)
        transition = calculate_transition_phase(v1)
        total_takeoff = calculate_takeoff_length(v1)
        accelerate_stop = calculate_accelerate_stop(v1)
        landing_length = calculate_landing_length(v1)

        # Append results to lists
        ground_run_distances.append(ground_run)
        transition_distances.append(transition)
        total_takeoff_lengths.append(total_takeoff)
        accelerate_stop_distances.append(accelerate_stop)
        landing_lengths.append(landing_length)

    # Plot Ground Run Distance vs. Decision Velocity
    plt.figure(figsize=(12, 6))
    plt.plot(v1_range, ground_run_distances, label="Ground Run Distance", color='blue')
    plt.plot(v1_range, transition_distances, label="Transition Phase Distance", color='green')
    plt.plot(v1_range, total_takeoff_lengths, label="Total Takeoff Distance", color='orange')
    plt.plot(v1_range, accelerate_stop_distances, label="Accelerate-Stop Distance", color='red')
    plt.plot(v1_range, landing_lengths, label="Landing Length", color='purple')

    # Customize the plot
    plt.title("Aircraft Runway Performance vs. Decision Velocity")
    plt.xlabel("Decision Velocity (m/s)")
    plt.ylabel("Distance (m)")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()
    
    

