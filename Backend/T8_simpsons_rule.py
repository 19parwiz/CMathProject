import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Function to integrate
def f(x):
    return np.sin(x)

# Simpson's 1/3 Rule Implementation
def simpsons_rule(a, b, n):
    if n % 2 == 1:  # Ensure n is even
        raise ValueError("Number of subintervals (n) must be even for Simpson's 1/3 Rule.")
    
    h = (b - a) / n  # Step size
    x = np.linspace(a, b, n + 1)  # n+1 points from a to b
    y = f(x)
    
    # Apply Simpson's 1/3 Rule Formula
    integral = (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])
    
    return integral, x, y  # Return the x and y points for plotting

# Given limits and subintervals
a, b = 0, np.pi
n = 10  # Given number of subintervals

# Compute the integral using Simpson's 1/3 Rule
simpsons_result, x_points, y_points = simpsons_rule(a, b, n)

# Compute exact integral using SciPy for verification
exact_result, _ = spi.quad(f, a, b)

# Compute error percentage
error_percentage = abs((exact_result - simpsons_result) / exact_result) * 100

# Print results
print(f"Simpson's 1/3 Rule Approximation: {simpsons_result}")
print(f"Exact Integral Value: {exact_result}")
print(f"Absolute Error: {abs(exact_result - simpsons_result)}")
print(f"Error Percentage: {error_percentage:.6f}%")

# ---- Plot the Function and Approximated Points ----
x_real = np.linspace(a, b, 100)
y_real = f(x_real)

plt.figure(figsize=(8, 5))
plt.plot(x_real, y_real, label=r"$\sin(x)$", color='blue')  # Actual function
plt.scatter(x_points, y_points, color='red', label="Simpson's Rule Points", zorder=3)  # Simpson's rule sample points
plt.fill_between(x_real, y_real, alpha=0.2, color='blue')  # Shaded integral region

plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Simpson's 1/3 Rule Approximation of Integral")
plt.legend()
plt.grid(True)
plt.show()
