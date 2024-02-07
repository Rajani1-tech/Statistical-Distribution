
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
class BetaDistributionModel:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def distribution(self):
        return beta(self.alpha, self.beta)

    def plot_pdf(self):
        x = np.linspace(0, 1, 1000)
        y = self.distribution().pdf(x)
        plt.plot(x, y, color='pink')
        plt.title('Beta Distribution PDF')
        plt.xlabel('x')
        plt.ylabel('PDF')
        plt.legend()
        plt.show()


model = BetaDistributionModel(5, 2)
model.plot_pdf()

