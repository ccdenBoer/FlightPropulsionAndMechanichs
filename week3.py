import matplotlib.pyplot as plt
import numpy as np
import math

def powerRequiredCurve(x):

    a = 0.0494
    rho = 1.225
    S = 361.6
    W = 217000
    b = 0.03164114177

    return (a * rho * S)/(2) * x**3 + (2 * b * W**2)/(rho * x * S)

def graph():
    # Create a range of x values
    HGx = np.linspace(0, 200, 1000)  # 1000 points between 0 and 200
    # Compute the corresponding y values
    HGy = powerRequiredCurve(HGx)


    # Plot the function
    plt.figure(figsize=(10, 10))
    plt.plot(HGx, HGy, label=r"Power Required Curve", color='blue')

    
    plt.axhline(0, color='black', linewidth=0.7, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=0.7, linestyle='--')  # y-axis
    plt.title("Power Required Curve")
    plt.xlabel("V [m/s]")
    plt.ylabel("Prh [W]")
    plt.grid(True)
    plt.legend()