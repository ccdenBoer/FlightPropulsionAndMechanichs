import math
import numpy as np
import matplotlib.pyplot as plt

def CalculateRadius(Velocity, phi):
    g = 9.81
    return (Velocity**2)/(g*math.tan(math.radians(phi)))

def CalculateTurningTime(Velocity, radius):
    return (2*math.pi*radius)/Velocity

def CalculateLoadFactor(phi):
    return 1/math.cos(math.radians(phi))

def graph_Radius():
    phi_range = np.linspace(1, 90, 90)  # Banking angles from 1° to 80°
    velocity = 244  # Constant speed (m/s)
    
    radii = [CalculateRadius(velocity, phi) for phi in phi_range]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(phi_range, radii, label="Radius", color='blue')
    plt.title("Radius vs Banking Angle at a constant speed of 244 m/s")
    plt.xlabel("Banking Angle (°)")
    plt.ylabel("Radius (m)")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    #plt.show()

# Graph: Turning Time vs. Banking Angle
def graph_TurningTime():
    phi_range = np.linspace(1, 90, 90)  # Banking angles from 1° to 80°
    velocity = 244  # Constant speed (m/s)
    
    radii = [CalculateRadius(velocity, phi) for phi in phi_range]
    turning_times = [CalculateTurningTime(velocity, r) for r in radii]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(phi_range, turning_times, label="Turning Time", color='green')
    plt.title("Turning Time vs Banking Angle at a constant speed of 244 m/s")
    plt.xlabel("Banking Angle (°)")
    plt.ylabel("Turning Time (s)")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    #plt.show()

# Graph: Load Factor vs. Banking Angle
def graph_LoadFactor():
    phi_range = np.linspace(1, 89, 90)  # Banking angles from 1° to 80°
    load_factors = [CalculateLoadFactor(phi) for phi in phi_range]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(phi_range, load_factors, label="Load Factor", color='purple')
    plt.title("Load Factor vs Banking Angle")
    plt.xlabel("Banking Angle (°)")
    plt.ylabel("Load Factor (G)")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    #plt.show()