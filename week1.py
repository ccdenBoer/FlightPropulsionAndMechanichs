import matplotlib.pyplot as plt
import numpy as np
import math

def dragPolar(y):
    return 0.0391 + (y**2)/(3.14*0.703*10.06)

def dragPolar2(x):
  
    B = 1 / (3.14 * 10.06 * 0.703)
    H = 1.237198
    M = 0.8 * H
    R = 0.2 * H
    K = 1.5 * dragPolar(H) - dragPolar(M)
    X = x - dragPolar(M)
    Q = 0
    P = K/(2*B*M)

    return (P + Q - 2 * R) * (X/K)**3 + (3 * R - 2 * P - Q) * (X/K)**2 + P * (X/K) + M

def dragPolar3(x):
    return (((x-0.1428262)**2) * -50) + 1.24

def graph():
    # Create a range of x values
    y = np.linspace(-0.1, 0.989758, 500)  # 500 points between -10 and 10
    # Compute the corresponding y values
    x = dragPolar(y)

    # Create a range of x values
    x2 = np.linspace(0.083192, 0.1428262, 500)  # 500 points between -10 and 10
    # Compute the corresponding y values
    y2 = dragPolar2(x2)

    # Create a range of x values
    x3 = np.linspace(0.1428262, 0.24, 500)  # 500 points between -10 and 10
    # Compute the corresponding y values
    y3 = dragPolar3(x3)


    # Plot the function
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, label=r"Drag polar", color='blue')
    plt.plot(x2, y2, label=r"Drag polar", color='blue')
    plt.plot(x3, y3, label=r"Drag polar", color='blue')
    plt.plot(0.14283,1.24,'ro') 
    plt.plot(0.0391, 0,'ro') 
    plt.plot(0.08319,0.98976,'ro') 
    plt.axhline(0, color='black', linewidth=0.7, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=0.7, linestyle='--')  # y-axis
    plt.title("Plot of Drag polar")
    plt.xlabel("Cl")
    plt.ylabel("Cd")
    plt.grid(True)
    plt.legend()