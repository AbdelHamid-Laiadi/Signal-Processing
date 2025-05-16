# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:54:01 2023

@author: HAMID

This code generates two sets of random data and then plots their
cross-correlation and the autocorrelation of one set using two
stacked subplots. It uses matplotlib to visualize how the two
signals relate to each other at different time lags, with 
grids and normalized values for clarity.

"""

import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(19680801)


x, y = np.random.randn(2, 100)
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)

plt.show()