#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:54:59 2023

@author: mukeshavudaiappan
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# Read data from CSV file
data_file = "data1.csv"
weights = []
with open(data_file, 'r') as f:
    reader = csv.reader(f)
    ##next(reader) # skip header row
    for row in reader:
        weight = float(row[0])
        weights.append(weight)
weights = np.array(weights)

# Create histogram of weights
n, bins, patches = plt.hist(weights, bins=30, density=True, alpha=0.5, 
                            label='Distribution')

# Setting color
fracs = ((n**(1 / 5)) / n.max())
norm = colors.Normalize(fracs.min(), fracs.max())
 
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Calculate average weight
w_avg = np.mean(weights)

# Calculate X such that 33% of newborns are born above X
total_count = len(weights)
cumulative_distribution = np.cumsum(n * np.diff(bins))
index = np.searchsorted(cumulative_distribution, 0.67) # 0.67 = 67%
x = bins[index]

# Add labels and legend to plot
plt.xlabel('Weight (in kg)')
plt.ylabel('Probability')
plt.title('Distribution of Newborn Weights')
plt.xticks(rotation = 35, fontsize = 8)
plt.yticks(fontsize = 8)
plt.legend(loc='upper right')

# Add text to plot with values of w_avg and X
plt.text(4.8, 0.30, f'Average weight = {w_avg:.2f} kg')
plt.text(4.8, 0.22, f'Weight at 33% = {x:.2f} kg')

# Show plot
plt.legend()
plt.show()
plt.close()

