import matplotlib.pyplot as plt
import numpy as np
import math
import week1
import week2
import week3
import week4
import week5

#week1.graph()
#week2.graph()
#week3.graph()
#week4.graph()

# leave for the end
#plt.show()

speed = 244 # max cruise speed according to website
for i in range(1, 60):
    print(f"Speed: {speed} m/s, φ {i}°, Turning radius: {week5.CalculateRadius(speed, i)} m, Turning time: {week5.CalculateTurningTime(speed, week5.CalculateRadius(speed, i))} seconds, Load factor: {week5.CalculateLoadFactor(i)} G")
