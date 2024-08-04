import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Defining the function and integration boundary
def f(x):
    return x ** 2

a = 0  # Lower bound
b = 2  # Upper bound

# Creating a range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Creating a graph
fig, ax = plt.subplots()

# Drawing the function
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Setting up the graph
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and graph title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

def monte_carlo_integration(f, a, b, num_points=10000):
    """
    Perform Monte Carlo integration.
    """
    x_random = np.random.uniform(a, b, num_points)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

result_quad, error_quad = spi.quad(f, a, b)

result_mc = monte_carlo_integration(f, a, b)

print(f"Monte Carlo Integration Result: {result_mc}")
print(f"SciPy quad Function Result: {result_quad}")
