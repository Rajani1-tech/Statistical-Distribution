import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parameters for the exponential distribution
lam = 0.5  # Rate parameter (lambda)
size = 1000  # Number of random samples to generate

# Generate random numbers following an exponential distribution
exponential_data = np.random.exponential(scale=1/lam, size=size)

# Plot a histogram to visualize the exponential distribution
plt.hist(exponential_data, bins=30, density=True, color='pink', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution')
plt.grid(True)
plt.show()

