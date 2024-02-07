
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# parameters
lamba = 10
k = np.arange(0, 20)

# poisson distribution
pmf_values = poisson.pmf(k, lamba)

# plot
plt.bar(k, pmf_values, color='pink')
plt.title('Poisson Distribution')
plt.xlabel('Number of k')
plt.ylabel('Probability')
plt.xticks(k)
plt.grid(axis='y', alpha=0.75)
plt.show()




