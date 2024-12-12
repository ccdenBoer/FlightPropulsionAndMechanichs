import matplotlib.pyplot as plt
import numpy as np
import math

a = 0.0494
rho = 1.225
S = 361.6
W = 217000
b = 0.03164114177

def powerRequiredCurveAtSeaLevel(x):

    rho = 1.225
    return (a * rho * S)/(2) * x**3 + (2 * b * W**2)/(rho * x * S)

def powerRequiredCurveAt10KFeet(x):

    rho = 1.1116 
    return (a * rho * S)/(2) * x**3 + (2 * b * W**2)/(rho * x * S)

def powerRequiredCurveAt30KFeet(x):

    rho = 0.459
    return (a * rho * S)/(2) * x**3 + (2 * b * W**2)/(rho * x * S)

def powerAvailableCurve(x):

    return 316000 * x

def graph():
    # Create a range of x values
    HGx = np.linspace(0, 300, 1000)  # 1000 points between 0 and 400
    # Compute the corresponding y values
    HGSeaLevel = powerRequiredCurveAtSeaLevel(HGx)
    HG10KFeet = powerRequiredCurveAt10KFeet(HGx)
    HG30KFeet = powerRequiredCurveAt30KFeet(HGx)

    HGa = powerAvailableCurve(HGx)


    # Plot the function
    plt.figure(figsize=(10, 10))
    plt.plot(HGx, HGSeaLevel, label=r"Sea level", color='lightblue')
    plt.plot(HGx, HG10KFeet, label=r"10.000 Feet", color='blue')
    plt.plot(HGx, HG30KFeet, label=r"30.000 Feet", color='darkblue')

    plt.plot(HGx, HGa, label=r"Thrust Available", color="red")

    # Highlight intersection
    intersectionsSeaLevel = np.argwhere(np.diff(np.sign(HGSeaLevel - HGa))).flatten()
    intersections10KFeet = np.argwhere(np.diff(np.sign(HG10KFeet - HGa))).flatten()
    intersections30KFeet = np.argwhere(np.diff(np.sign(HG30KFeet - HGa))).flatten()
    
    plt.plot(HGx[intersectionsSeaLevel], HGa[intersectionsSeaLevel], 'ro')
    plt.plot(HGx[intersections10KFeet], HGa[intersections10KFeet], 'ro')
    plt.plot(HGx[intersections30KFeet], HGa[intersections30KFeet], 'ro')


    plt.axhline(0, color='black', linewidth=0.7, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=0.7, linestyle='--')  # y-axis
    plt.title("Power Required Curve")
    plt.xlabel("V [m/s]")
    plt.ylabel("Prh [W]")
    plt.grid(True)
    plt.legend()