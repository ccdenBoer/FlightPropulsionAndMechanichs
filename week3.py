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

def climbRateAtSeaLevel(x):
    
    return ((powerAvailableCurve(x) - powerRequiredCurveAtSeaLevel(x)) / 217000)    

def climbRateAt10KFeet(x):

    return ((powerAvailableCurve(x) - powerRequiredCurveAt10KFeet(x)) / 217000)    

def climbRateAt30KFeet(x):

    return ((powerAvailableCurve(x) - powerRequiredCurveAt30KFeet(x)) / 217000)    

def graph():
    # Create a range of x values
    HGx = np.linspace(0, 300, 1000)  # 1000 points between 0 and 300
    # Compute the corresponding y values
    HGSeaLevel = powerRequiredCurveAtSeaLevel(HGx)
    HG10KFeet = powerRequiredCurveAt10KFeet(HGx)
    HG30KFeet = powerRequiredCurveAt30KFeet(HGx)

    cSeaLevel = climbRateAtSeaLevel(HGx)
    c10KFeet = climbRateAt10KFeet(HGx)
    c30KFeet = climbRateAt30KFeet(HGx)

    HGa = powerAvailableCurve(HGx)

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(10, 10))

    # Plot power curves on the primary y-axis
    ax1.plot(HGx, HGSeaLevel, label="Power Required (Sea level)", color='lightblue')
    ax1.plot(HGx, HG10KFeet, label="Power Required (10,000 Feet)", color='blue')
    ax1.plot(HGx, HG30KFeet, label="Power Required (30,000 Feet)", color='darkblue')
    ax1.plot(HGx, HGa, label="Thrust Available", color="red")

    # Highlight intersections
    intersectionsSeaLevel = np.argwhere(np.diff(np.sign(HGSeaLevel - HGa))).flatten()
    intersections10KFeet = np.argwhere(np.diff(np.sign(HG10KFeet - HGa))).flatten()
    intersections30KFeet = np.argwhere(np.diff(np.sign(HG30KFeet - HGa))).flatten()

    ax1.plot(HGx[intersectionsSeaLevel], HGa[intersectionsSeaLevel], 'ro')
    ax1.plot(HGx[intersections10KFeet], HGa[intersections10KFeet], 'ro')
    ax1.plot(HGx[intersections30KFeet], HGa[intersections30KFeet], 'ro')

    ax1.set_xlabel("V [m/s]")
    ax1.set_ylabel("Power [W]", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    # Create secondary y-axis for climb rates
    ax2 = ax1.twinx()
    ax2.plot(HGx, cSeaLevel, label="Climb Rate (Sea level)", color='lightgreen', linestyle='-')
    ax2.plot(HGx, c10KFeet, label="Climb Rate (10,000 Feet)", color='green', linestyle='--')
    ax2.plot(HGx, c30KFeet, label="Climb Rate (30,000 Feet)", color='darkgreen', linestyle='--')
    ax2.set_ylabel("Climb Rate [m/s]", color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Combine legends from both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    legend = ax2.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
    legend.set_zorder(15)  # Bring legend to the front

    plt.title("Power Required and Climb Rate Curves")