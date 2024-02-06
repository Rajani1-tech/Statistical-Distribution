
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# parameters for the normal distribution
mean = 0 
std_dev = 1 
num_samples = 1000

# generate random numbers following a normal distribution
data = np.random.normal(mean, std_dev, num_samples)

# plot the histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='pink')

# plot the PDF of normal distribution
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)

# adding labels and title
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.show()


