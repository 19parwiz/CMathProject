import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

            # we defined the functin here  f(x) = x^4 - 10x^2 + 9
def f(x):
    return x**4 - 10*x**2 + 9  

               # Function for plotting the graph of f(x) within the interval [-4, 40]
def draw_graph():
    x = np.linspace(-4, 4, 400)  # Generate 400 points between -4 and 4
    y = f(x)       
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$f(x) = x^4 - 10x^2 + 9$', color='blue')
    
    # Add reference lines for better visualization
    plt.axhline(0, color='black', linewidth=1, linestyle='--')      # the x axiz 
    plt.axvline(0, color='black', linewidth=1, linestyle='--')      # the y axiz 
    
    plt.grid()  
    plt.legend()        # Display function label
    plt.title("Graph of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()          # Showing  the plot

                        # we need to find the  roots using numerical approximation
def numerical_roots():
                # We use multiple initial guesses to find all roots
    initial_guesses = [-3.5, -1.5, 1.5, 3.5] 
    roots = fsolve(f, initial_guesses) 
    return np.round(roots, 5)  

            # counting the absolute error between graphical and numerical root
def compute_absolute_errors(graphical_roots, numerical_roots):
    errors = [abs(n - g) for g, n in zip(graphical_roots, numerical_roots)]
    return np.round(errors, 5)  # Round error values for clarity

if __name__ == "__main__":
    draw_graph()  
    
            # Approximate roots from graph inspection
    graphical_approximate_roots = [-3, -1, 1, 3]
    
                            # Find numerical roots
    num_roots = numerical_roots()
    
                # Computein the errors
    errors = compute_absolute_errors(graphical_approximate_roots, num_roots)
    
    # Display the  results here
    print("=== Root Finding Results here ===")
    print(f"Estimation from our graph: {graphical_approximate_roots}")
    print(f"Roots from calculations (fsolve): {num_roots}")
    print(f"Absolute Error: {errors}")
