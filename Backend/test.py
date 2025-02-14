# task1_graphical_method.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return x**4 - 10*x**2 + 9

def plot_graph():
    x = np.linspace(-4, 4, 400)
    y = f(x)
    plt.plot(x, y, label=r'$f(x) = x^4 - 10x^2 + 9$')
    plt.axhline(0, color='black', linewidth=1, linestyle='--')
    plt.grid()
    plt.legend()
    plt.title("Graph of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

def numerical_root():
    initial_guess = 2
    root = fsolve(f, initial_guess)
    return root[0]

def compute_absolute_error(graphical_root, numerical_root):
    return abs(numerical_root - graphical_root)

def run_task1():
    print("Task 1: Graphical Method and Absolute Error")
    plot_graph()
    graphical_approximate_root = float(input("Enter the approximate root from the graph: "))
    num_root = numerical_root()
    error = compute_absolute_error(graphical_approximate_root, num_root)
    print(f"Graphical Approximate Root: {graphical_approximate_root}")
    print(f"Numerical Root (fsolve): {num_root}")
    print(f"Absolute Error: {error}")