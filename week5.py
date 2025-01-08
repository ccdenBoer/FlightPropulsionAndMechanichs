import math

def CalculateRadius(Velocity, phi):
    g = 9.81
    return (Velocity**2)/(g*math.tan(math.radians(phi)))

def CalculateTurningTime(Velocity, radius):
    return (2*math.pi*radius)/Velocity

def calculateLoadFactor(phi):
    return 1/math.cos(math.radians(phi))