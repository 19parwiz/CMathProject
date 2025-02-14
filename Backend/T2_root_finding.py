
import math 

def f(x):
    """Define the function whose root we want to find."""
    return x**3 - 6*x**2 + 11*x - 6  # Example function

def bisection_method(a, b, tol=1e-6, max_iter=100):
    """Finds a root of f(x) using the Bisection Method."""
    if f(a) * f(b) >= 0:
        print(f"Bisection method fails: f({a}) = {f(a)}, f({b}) = {f(b)}")
        return None  # No valid root in this interval
    
    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2  # Midpoint
        if f(c) == 0:  # If c is a root, stop
            return c, iterations
        elif f(a) * f(c) < 0:  # Root is in left subinterval
            b = c
        else:  # Root is in right subinterval
            a = c
        iterations += 1

    return (a + b) / 2, iterations  # Return the approximate root and iteration count

#  Step 1: Define an interval where f(a) and f(b) have opposite signs
a, b = 0, 4  # Choose a correct interval

#  Step 2: Print function values before running the method
print(f"f({a}) = {f(a)}, f({b}) = {f(b)}")

#  Step 3: Run the Bisection Method and check if result is valid
result = bisection_method(a, b)

if result is not None:
    bisect_root, bisect_iter = result
    print(f"Root found: {bisect_root:.6f} after {bisect_iter} iterations")
else:
    print("No valid root found in the given interval.")
