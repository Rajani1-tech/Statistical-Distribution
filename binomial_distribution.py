
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# parameters for the binomial distribution
n = 10   # number of trials
p = 0.5  # probability of success

# generate a range of possible values for no. of successes
k_values = np.arange(0, n+1)

# calculate PMF for each values of k
pmf_values = binom.pmf(k_values, n, p)

# plot the PMF
plt.bar(k_values, pmf_values, color='pink')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution')
plt.xticks(k_values)
plt.show()


