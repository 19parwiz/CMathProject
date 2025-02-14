def relaxation_method(omega=0.5, tol=1e-6, max_iter=100):
    x, y, z = 0, 0, 0  # Initial guesses

    for iteration in range(max_iter):
        x_new = (1 - omega) * x + omega * (10 - y - z)
        y_new = (1 - omega) * y + omega * (8 - z)
        z_new = (1 - omega) * z + omega * (6 - x)

        # Print every 10 iterations
        if iteration % 10 == 0:
            print(f"Iteration {iteration}: x={x_new:.6f}, y={y_new:.6f}, z={z_new:.6f}")

        # Check for convergence
        if abs(x_new - x) < tol and abs(y_new - y) < tol and abs(z_new - z) < tol:
            return x_new, y_new, z_new, iteration + 1

        x, y, z = x_new, y_new, z_new  # Update values

    return x, y, z, max_iter  # Return max iterations reached 

# Run the method
solution_x, solution_y, solution_z, iterations = relaxation_method()
print(f"Solution: x = {solution_x:.6f}, y = {solution_y:.6f}, z = {solution_z:.6f} (Converged in {iterations} iterations)")
