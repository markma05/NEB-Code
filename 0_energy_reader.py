# ===============================================
# NEB OUTCAR Energy Reader

# Last updated: 2021/4/30
# Written by Mark Ma, Yiqing Wang

# The program is used to extract entropy-included total energy from NEB calculations.
# The program is designed to process VASP output only, with IMAGES < 10
# ===============================================

# ===============================================
# Import libraries
# ===============================================
#import numpy as np
#import math

# ===============================================
# Set Variables
# ===============================================
# Number of NEB Images
image = 8

# Header of OUTCAR files that can be skipped
skip_header = 15000

# Minimum distance between two energy tags that can be skipped
skip_lines = 28

# ===============================================
# Code begins here
# ===============================================
# Define Output
F_list = []
E_list = []
# Define file path
for i in range(image):
    input_path = "0" + str(i + 1) + "/OUTCAR"

    # Open each individual file and skip header
    with open(input_path, "r") as input_file:
        lines = input_file.readlines()[skip_header:]

        # Read through every line
        index = 2 + int((0.9 * len(lines) ) // 1)
        while (index < len(lines)):
            line_E = lines[index]
            line_F = lines[index - 2]
            if (line_E.strip().startswith("energy without")):
                energy_no_entropy = 0.0
                energy_no_entropy = line_E.strip().split()[4]

                energy_entropy = 0.0
                energy_entropy = line_F.strip().split()[4]

                index += skip_lines
            else:
                index += 1

    E_list.append(energy_no_entropy)
    F_list.append(energy_entropy)

output_path = "0_free_energy.txt"
with open(output_path, "w+") as output_file:
    for i in range(image):
            output_file.write(str(i + 1) + "\t" + str(F_list[i]) + "\t" + str(E_list[i]) + "\n")
