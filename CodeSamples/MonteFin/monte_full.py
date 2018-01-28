import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define Variables
#S = apple['Adj Close'][-1]  # starting stock price (i.e. last available real stock price)
S = 171.51
T = 252  # Number of trading days
mu = 0.2309  # Return
vol = 0.4259  # Volatility

# choose number of runs to simulate - I have chosen 1000
for i in range(1000):
    # create list of daily returns using random normal distribution
    daily_returns = np.random.normal(mu / T, vol / math.sqrt(T), T) + 1

    # set starting price and create price series generated by above random daily returns
    price_list = [S]

    for x in daily_returns:
        price_list.append(price_list[-1] * x)

    # plot data from each individual run which we will plot at the end
    plt.plot(price_list)

# show the plot of multiple price series created above
plt.show()