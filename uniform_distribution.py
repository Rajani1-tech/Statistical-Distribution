
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the uniform distribution
a = 0  # Lower bound of the interval
b = 100  # Upper bound of the interval
x = 50  # Number of unique random samples to generate

# uniform distribution
values = np.linspace(a, b, 1000)
pdf_values = np.ones_like(values) / (b - a)

# Plot
plt.plot(values, pdf_values, label='Uniform Distribution')
plt.fill_between(values, pdf_values, where=(values < x), color='pink',
                 alpha=0.5, label='Area under the curves(x<50)')
plt.legend()
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.title('Uniform Distribution')
plt.grid(axis='y')
plt.show()


