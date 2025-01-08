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
muBrake = 0.4
CD = 0.0233  # drag coefficient
CL = 0.15  # lift coefficient (for takeoff)
S = 122.6  # wing area (m^2)
V_LOF = 80.0  # lift-off velocity (m/s)

# Function to calculate the ground roll distance
def calculate_ground_run(v1):
    p = g * ((T / W) - mu)
    q = -(g * (CD - mu * CL) * rho * S) / (2 * W)

    ln_term = math.log(p + (q * (v1**2))) - math.log(p)
    ground_roll_distance = (1 / (2 * q)) * ln_term
    return ground_roll_distance

def calculate_ground_run_OEI(v1):
    p = g * (((T/2) / W) - mu)
    q = -(g * (CD - mu * CL) * rho * S) / (2 * W)

    ln_term = math.log(p + (q * (v1**2))) - math.log(p)
    ground_roll_distance = (1 / (2 * q)) * ln_term
    return ground_roll_distance

def calculate_transition_phase(v1):
    # Calculate lift and drag
    L = CL * rho * ((v1**2) / 2) * S
    D = CD * rho * ((v1**2) / 2) * S

    R = (W * (v1**2)) / (g * ((W * 1.1) - W))

    gamma = (T - D) / W  # Compute gamma
    gamma_in_radians = gamma * (math.pi / 180)  # Convert gamma to radians
    s_b = R * gamma_in_radians  # Use gamma in radians

    return s_b 

def calculate_transition_phase_OEI(v1):
    # Calculate lift and drag
    L = CL * rho * ((v1**2) / 2) * S
    D = CD * rho * ((v1**2) / 2) * S

    R = (W * (v1**2)) / (g * ((W * 1.1) - W))

    gamma = ((T/2) - D) / W  # Compute gamma
    gamma_in_radians = gamma * (math.pi / 180)  # Convert gamma to radians
    s_b = R * gamma_in_radians  # Use gamma in radians

    return s_b 

def calculate_brake_run(v1):
    p = g * ((T / W) - mu)
    q = -(g * (CD - mu * CL) * rho * S) / (2 * W)

    ln_term = math.log(p + (q * (v1**2))) - math.log(p)
    ground_roll_distance = (1 / (2 * q)) * ln_term
    return ground_roll_distance

# Function to calculate accelerate-stop distance
def calculate_accelerate_stop(v1):
    accelerate = calculate_ground_run(v1)
    decelerate = calculate_brake_run(v1)
    return accelerate + decelerate

# Function to calculate the total runway length for AEO/OEI scenarios
def calculate_takeoff_length_AEO(v1):
    ground_run = calculate_ground_run(v1)
    transition = calculate_transition_phase(v1)
    total_runway_length = ground_run + transition
    return total_runway_length

# Function to calculate the total runway length for AEO/OEI scenarios
def calculate_takeoff_length_OEI(v1):
    ground_run = calculate_ground_run_OEI(v1)
    transition = calculate_transition_phase_OEI(v1)
    total_runway_length = ground_run + transition
    return total_runway_length

# Function to calculate the landing runway length
def calculate_landing_length(v1):
    screen_height = 15.24 #50 ft to meter
    flare_height = 12.20

    # 3 degrees is a standard ILS
    final_approach_distance = (screen_height - flare_height) / math.tan(3)
    flare = calculate_flare_phase(v1)
    landing_run = calculate_ground_run_landing(v1)

    return final_approach_distance + flare + landing_run

#reverse trust at 80%
def calculate_ground_run_landing(v1):
    p = g * ((T / W) - mu)
    q = -(g * (CD - mu * CL) * rho * S) / (2 * W)

    ln_term = math.log(p + (q * (v1**2))) - math.log(p)
    ground_roll_distance = (1 / (2 * q)) * ln_term
    return ground_roll_distance

def calculate_flare_phase(v1):
    # Calculate lift and drag
    L = CL * rho * ((v1**2) / 2) * S
    D = CD * rho * ((v1**2) / 2) * S

    R = (W * (v1**2)) / (g * ((W * 1.1) - W))

    gamma = (T - D) / W  # Compute gamma
    gamma_in_radians = gamma * (math.pi / 180)  # Convert gamma to radians
    s_b = R * gamma_in_radians  # Use gamma in radians

    return s_b 

def graph():
    v1_range = np.linspace(40, 80, 50)  # Range of decision velocities (m/s)

    # Initialize lists to store results
    total_takeoff_lengths_AEO = []
    total_takeoff_lengths_OEI = []
    accelerate_stop_distances = []
    landing_lengths = []

    # Loop through each velocity in the range
    for v1 in v1_range:
        total_takeoff_length_AEO = calculate_takeoff_length_AEO(v1)
        total_takeoff_length_OEI = calculate_takeoff_length_OEI(v1)
        accelerate_stop = calculate_accelerate_stop(v1)
        landing_length = calculate_landing_length(v1)

        # Append results to lists
        total_takeoff_lengths_AEO.append(total_takeoff_length_AEO)
        total_takeoff_lengths_OEI.append(total_takeoff_length_OEI)
        accelerate_stop_distances.append(accelerate_stop)
        landing_lengths.append(landing_length)

    # Plot Ground Run Distance vs. Decision Velocity
    plt.figure(figsize=(12, 6))
    #plt.plot(v1_range, total_takeoff_lengths_AEO, label="AEO", color='blue')
    #plt.plot(v1_range, total_takeoff_lengths_OEI, label="OEI", color='green')
    #plt.plot(v1_range, accelerate_stop_distances, label="Accelerate-Stop Distance", color='red')
    plt.plot(v1_range, landing_lengths, label="Landing Length", color='purple')

    # Customize the plot
    plt.title("Required Runway Length vs Approach Speed")
    plt.xlabel("Approach speed (m/s)")
    plt.ylabel("Distance (m)")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    #plt.show()
    
    

