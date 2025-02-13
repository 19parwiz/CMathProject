import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Given data points
x = np.array([0, 0.5, 1.0, 1.5])
y = np.array([0, 0.25, 0.75, 2.25])

# Perform cubic spline interpolation
cs = CubicSpline(x, y)

# Generate finer x values for smooth curve
x_fine = np.linspace(0, 1.5, 100)
y_fine = cs(x_fine)

# Plot the results
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fine, y_fine, label='Cubic Spline', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Cubic Spline Interpolation')
plt.grid()
plt.show()
