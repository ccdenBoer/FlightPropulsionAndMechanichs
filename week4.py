import matplotlib.pyplot as plt
import numpy as np
import math

Nacc = 0.015
Ndec = 0.40
g = 9.81
W = 217000
rho = 1.225
S = 361.6
T = 310 * 2 * 1000
b= 60.3

def TakeOffPhaseGroundRunAcc(V):
    Cd = 0.0391
    Cl = Nacc/(2*b)
    p = g*((T/W)-Nacc)
    q = -(g*(Cd - Nacc*Cl)*rho*S)/(2*W)
    a = p+q*(V**2)
    return a

def TakeOffPhaseGroundRunDec(V):
    Cd = 0.0391
    Cl = Ndec/2*b
    p = g*((T/W)-Ndec)
    q = -(g*(Cd - Ndec*Cl)*rho*S)/2*W
    a = p+q*(V**2)
    return a

def CalcVelocity(v): 
    exitvalue = 242 / 3.6
    print (v)
    v += TakeOffPhaseGroundRunAcc(v)
    if v >= exitvalue or v < 0: return
    v = CalcVelocity(v) 
    return v

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