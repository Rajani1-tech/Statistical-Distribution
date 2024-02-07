
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

def plot_weibull_cdf(scale, shape):
    x = np.linspace(0, 10, 1000)
    cdf = weibull_min.cdf(x, shape, scale=scale)
    plt.figure(figsize=(8, 6))
    plt.plot(x, cdf, color='pink')
    plt.title('Weibull Distribution CDF')
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_weibull_cdf(scale=1.5, shape=3)
