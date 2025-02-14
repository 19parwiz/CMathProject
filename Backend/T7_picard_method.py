import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#       Define variables
x = sp.Symbol('x')

#           Given differential equation: dy/dx = x + y
f = x + sp.Symbol('y')

# Initial condition: y(0) = 1
y0 = 1



            # Picard's Iterations (Explicitly Evaluating Integrals)
y1 = y0 + sp.integrate(x + y0, x)  #    First approximation
y2 = y0 + sp.integrate(x + y1, x)  #    the second 
y3 = y0 + sp.integrate(x + y2, x)       #        the 3th 
y4 = y0 + sp.integrate(x + y3, x)       #           the 4th 




#               Converting the symbolic expressions to functions
y1_func = sp.lambdify(x, y1, 'numpy')
y2_func = sp.lambdify(x, y2, 'numpy')
y3_func = sp.lambdify(x, y3, 'numpy')
y4_func = sp.lambdify(x, y4, 'numpy')



        # Evaluate y(0.2)
x_val = 0.2
y1_val = y1_func(x_val)
y2_val = y2_func(x_val)
y3_val = y3_func(x_val)
y4_val = y4_func(x_val)



# Print results
print(f"y1(0.2) = {y1_val}")
print(f"y2(0.2) = {y2_val}")
print(f"y3(0.2) = {y3_val}")
print(f"y4(0.2) = {y4_val}")

# Plot results
x_vals = np.linspace(0, 1, 100)
plt.plot(x_vals, y1_func(x_vals), label="1st Approximation", linestyle='dotted')
plt.plot(x_vals, y2_func(x_vals), label="2nd Approximation", linestyle='dashed')
plt.plot(x_vals, y3_func(x_vals), label="3rd Approximation", linestyle='dashdot')
plt.plot(x_vals, y4_func(x_vals), label="4th Approximation", linestyle='solid')



# Mark the point (0.2, y4(0.2))
plt.scatter([0.2], [y4_val], color='red', zorder=3, label="y(0.2) at 4th Approximation")


# Graph details
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Picard's Method Approximations")
plt.legend()
plt.grid(True)
plt.show()
