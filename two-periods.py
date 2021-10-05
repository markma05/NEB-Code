# Last updated: 2021/10/04
# Written by Mark Ma

# A program that investigates the minimal required space to fit two periodic systems
# Designed for the GR-Ge project
# ==========================================================

# ==================================================
# Import Libraries
# ==================================================
import numpy as np
import sys

# ==================================================
# Set variables
# ==================================================
# Size of two periodic systems
seg_long = 24.85
seg_short = 23.57

# Number of data points
n_data = 100

# Starting point
n_start = 3

# ==================================================
#  Program starts here
# ==================================================
# A list of result values
result_abs = []
result_frac = []
result_index = []

for i in range (n_start, n_data + n_start):
    l_long = 0.0
    l_long = i * seg_long
    n_short = np.floor_divide(l_long, seg_short)
    delta_l = min((l_long - n_short*seg_short), (n_short*seg_short + seg_short - l_long))
    delta_frac = delta_l / l_long

    result_abs.append(delta_l)
    result_frac.append(delta_frac)
    result_index.append(i)

output_path = "result.txt"
with open(output_path, "w+") as output_file:
    for i in range(n_data):
            output_file.write(str(result_index[i]) + "\t" + str(result_abs[i]) + "\t" + str(result_frac[i]) + "\n")


