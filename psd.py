# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:16:03 2023

@author: HAMID
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 10, dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(40 * np.pi * t) + cnse


plt.subplot(211)
plt.plot(t, s)
plt.subplot(212)
plt.psd(s, 512,  1/ dt)

plt.show()