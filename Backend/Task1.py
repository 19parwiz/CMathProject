import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    """Function f(x) = x^4 - 10x^2 + 9"""
    return x**4 - 10*x**2 + 9

def plot_graph():
    """Plots the function f(x) in the range [-4,4]"""
    x = np.linspace(-4, 4, 400)  # Generate x values
    y = f(x)  # Compute f(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$f(x) = x^4 - 10x^2 + 9$')
    plt.axhline(0, color='black', linewidth=1, linestyle='--')  # x-axis
    plt.axvline(0, color='black', linewidth=1, linestyle='--')  # y-axis
    plt.grid()
    plt.legend()
    plt.title("Graph of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

def numerical_root():
    """Finds a root of f(x) using a numerical method (fsolve)"""
    initial_guess = 2  # Start from x=2 (based on graph observation)
    root = fsolve(f, initial_guess)
    return root[0]  # fsolve returns an array, take the first element

def compute_absolute_error(graphical_root, numerical_root):
    """Computes absolute error |numerical_root - graphical_root|"""
    return abs(numerical_root - graphical_root)

if __name__ == "__main__":
    plot_graph()
    
    # Approximate root from the graph (estimate manually, e.g., 3)
    graphical_approximate_root = 3.0  
    
    # Find numerical root
    num_root = numerical_root()
    
    # Compute absolute error
    error = compute_absolute_error(graphical_approximate_root, num_root)
    
    print(f"Graphical Approximate Root: {graphical_approximate_root}")
    print(f"Numerical Root (fsolve): {num_root}")
    print(f"Absolute Error: {error}")
