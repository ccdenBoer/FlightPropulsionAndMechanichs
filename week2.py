import matplotlib.pyplot as plt
import numpy as np
import math

def holoGraph(x):

    a = 0.0494
    rho = 1.225
    S = 361.6
    W = 217000
    V = -x
    b = 0.03164114177

    return (a * rho * S)/(2 * W) * V**3 + (2 * b * W)/(rho * V * S)

def graph():
    # Create a range of x values
    HGx = np.linspace(0, 200, 1000)  # 500 points between -10 and 10
    # Compute the corresponding y values
    HGy = holoGraph(HGx)


    # Plot the function
    plt.figure(figsize=(10, 10))
    plt.plot(HGx, HGy, label=r"HoloGraph", color='blue')
    plt.plot(154,holoGraph(154),'ro') 
    plt.plot(9.2, holoGraph(9.2),'ro') 
    plt.axhline(0, color='black', linewidth=0.7, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=0.7, linestyle='--')  # y-axis
    plt.title("Plot of HoloGraph")
    plt.xlabel("m/s")
    plt.ylabel("m/s")
    plt.grid(True)
    plt.legend()