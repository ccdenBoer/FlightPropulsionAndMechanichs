import matplotlib.pyplot as plt
import numpy as np

def hodograph(x):
    a = 0.0494 
    rho = 1.225
    S = 361.6
    W = 217000
    b = 0.03164114177
    C = (((a * rho * S) / (2 * W)) * -x ** 3) + (2 * b * W) / (rho * -x * S)
    return C 

def graph():
    # Create a range of x values
    HGx = np.linspace(0.1, 200, 500)  # Avoid zero division error
    # Compute the corresponding y values
    HGy = hodograph(HGx)

    # Define special points
    x_points = np.array([9.2, 154])
    y_points = hodograph(x_points)

    # Plot the function
    plt.figure(figsize=(10, 10))
    plt.plot(HGx, HGy, label="Hodograph", color='blue')
    
    # Plot the special points
    plt.scatter(x_points, y_points, color='red', label="Special Points")
    for i, txt in enumerate(x_points):
        plt.annotate(f"({txt:.1f}, {y_points[i]:.2f})", (x_points[i], y_points[i]),
                     textcoords="offset points", xytext=(10,-10), ha='center')

    plt.axhline(0, color='black', linewidth=0.7, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=0.7, linestyle='--')  # y-axis
    plt.title("Plot of Hodograph")
    plt.xlabel("V [m/s]")
    plt.ylabel("C [m/s]")
    plt.grid(True)
    plt.legend()