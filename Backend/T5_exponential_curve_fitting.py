import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_func(x, a, b):
    return a * np.exp(b * x)



    # Given the data points here 
x_data = np.array([0, 1, 2, 3])
y_data = np.array([np.exp(0), np.exp(1), np.exp(2), np.exp(3)])  # [1, e, e^2, e^3]

                # We need  the exponential model
                
params, covariance = curve_fit(exponential_func, x_data, y_data)
a_fit, b_fit = params

#               Generate fitted curve
test_x = np.linspace(0, 3, 100)
test_y = exponential_func(test_x, a_fit, b_fit)



#                       Plot original data and fitted curve

plt.scatter(x_data, y_data, color='red', label='Data Points')
plt.plot(test_x, test_y, label=f'Fitted Curve: y = {a_fit:.4f}e^({b_fit:.4f}x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Curve Fitting')
plt.legend()
plt.grid()
plt.show()



# Print the estimated parameters
print(f"Estimated Parameters: a = {a_fit:.4f}, b = {b_fit:.4f}")
