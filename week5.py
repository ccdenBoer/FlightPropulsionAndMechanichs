import math
import numpy as np
import matplotlib.pyplot as plt

# Calculate the turning radius with the given velocity and angle (after converting to radians)
def CalculateRadius(Velocity, phi):
    g = 9.81 
    return (Velocity**2)/(g*math.tan(math.radians(phi)))

# Calculate the turning time with the given radius and velocity
def CalculateTurningTime(Velocity, radius):
    return (2*math.pi*radius)/Velocity 

# Calculate the load factor with the given angle (after converting to radians)
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

a = 0.0494
S = 361.6
W = 217000
b = 0.03164114177

def powerRequiredCurveAt10KFeet(V, phi):
    rho = 1.1116
    return ((a * rho * S)/(2)) * V**3 + (2 * b * W**2)/(rho * V * S * math.cos(math.radians(phi))**2)

def graph_powerRequired():
    # Create a range of x values
    HGx = np.linspace(0.2, 300, 1000)  # 1000 points between 0 and 300
    angle_1 = 30
    angle_2 = 45
    angle_3 = 60
    # Compute the corresponding y values
    HG30D = powerRequiredCurveAt10KFeet(HGx, angle_1)
    HG45D = powerRequiredCurveAt10KFeet(HGx, angle_2)
    HG60D = powerRequiredCurveAt10KFeet(HGx, angle_3)


    # Create the plot
    fig, ax1 = plt.subplots(figsize=(10, 10))

    # Plot power curves on the primary y-axis
    ax1.plot(HGx, HG30D, label="Power Required 30*", color='blue')
    ax1.plot(HGx, HG45D, label="Power Required 45*", color='green')
    ax1.plot(HGx, HG60D, label="Power Required 60*", color='red')

    ax1.set_xlabel("V [m/s]")
    ax1.set_ylabel("Power [W]", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    # Combine legends from both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    legend = ax1.legend(lines1, labels1, loc="upper right")
    legend.set_zorder(15)  # Bring legend to the front

    plt.title("Power Required")