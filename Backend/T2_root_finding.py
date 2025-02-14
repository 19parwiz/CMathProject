import math

# Define the function whose root we want to find
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Define the derivative of the function for Newton-Raphson
def df(x):
    return 3*x**2 - 12*x + 11

# Bisection Method
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

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    """Finds a root of f(x) using the Newton-Raphson Method."""
    iterations = 0
    while iterations < max_iter:
        f_x0 = f(x0)
        df_x0 = df(x0)
        
        if df_x0 == 0:  # Avoid division by zero
            print("Newton-Raphson method fails: Derivative is zero.")
            return None
        
        x1 = x0 - f_x0 / df_x0  # Newton-Raphson formula
        if abs(x1 - x0) < tol:  # Check for convergence
            return x1, iterations
        x0 = x1
        iterations += 1
    
    return x0, iterations  # Return the approximate root and iteration count

# Step 1: Define an interval where f(a) and f(b) have opposite signs
a, b = 0, 4  # Choose a correct interval

# Step 2: Print function values before running the method
print(f"f({a}) = {f(a)}, f({b}) = {f(b)}")

# Step 3: Run the Bisection Method and check if result is valid
bisect_result = bisection_method(a, b)

if bisect_result is not None:
    bisect_root, bisect_iter = bisect_result
    print(f"Bisection Method: Root found: {bisect_root:.6f} after {bisect_iter} iterations")
else:
    print("Bisection Method: No valid root found in the given interval.")

                # Step 4: Run the Newton-Raphson Method
x0 = 2.5         # Initial guess for Newton-Raphson
newton_result = newton_raphson(x0)

if newton_result is not None:
    newton_root, newton_iter = newton_result
    print(f"Newton-Raphson Method: Root found: {newton_root:.6f} after {newton_iter} iterations")
else:
    print("Newton-Raphson Method: No valid root found.")

            # Step 5: Compare the two methods
if bisect_result is not None and newton_result is not None:
    print("\n=== Comparison of Methods ===")
    print(f"Bisection Method: Root = {bisect_root:.6f}, Iterations = {bisect_iter}")
    print(f"Newton-Raphson Method: Root = {newton_root:.6f}, Iterations = {newton_iter}")