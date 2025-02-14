import numpy as np

def power_method(A, tol=1e-6, max_iterations=100):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    
    # Initial guess vector (can be randomized)
    x = np.ones(n)
    
    lambda_old = 0
    for i in range(max_iterations):
        # Matrix-vector multiplication
        x_new = np.dot(A, x)
        
        # Find the new eigenvalue approximation
        lambda_new = max(abs(x_new))
        
        # Normalize the new vector
        x_new = x_new / lambda_new
        
        # Check for convergence
        if abs(lambda_new - lambda_old) < tol:
            break
        
        x = x_new
        lambda_old = lambda_new
    
    return lambda_new, x

# Given matrix
A = np.array([[6, 2, 3],
              [2, 6, 4],
              [3, 4, 6]])

# Finding the largest eigenvalue and corresponding eigenvector
eigenvalue, eigenvector = power_method(A)

# Display the results
print(f"Largest Eigenvalue: {eigenvalue}")
print(f"Corresponding Eigenvector: {eigenvector}")
