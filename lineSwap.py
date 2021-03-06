# This is the number of line where the able begins
data_begin = 9
#This is where the 1st line is supposed to be swaped to
swap_pos = 5
# Number of images to be converted
n_im = 2

# This is the part of Pd layer that moves or not
n_fix_1 = 48
n_move_1 = 16
# This is the part of interstitial species
n_fix_2 = 16
# The function to turn on selective dynamics
def selectiveDynamics(lines):
    lines.insert(swap_pos + 2, "Selective dynamics \n")

    j = data_begin
    while j < (data_begin + n_fix_1):
        lines[j] = "  " + lines[j].strip() + "  " + "F F F\n"
        j += 1

    while j < (data_begin + n_fix_1 + n_move_1):
        lines[j] = "  " + lines[j].strip() + "  " + "T T T\n"
        j += 1

    while j < (data_begin + n_fix_1 + n_move_1 + n_fix_2):
        lines[j] = "  " + lines[j].strip() + "  " + "F F F\n"
        j += 1

    while j < len(lines):
        lines[j] = "  " + lines[j].strip() + "  " + "T T T\n"
        j += 1

    return lines

# Read the ten POSCAR files in the NEB folder,
# generated by ImageInterpolator
for i in range(n_im + 2):
    filename = "0" + str(i) + "/POSCAR"
    with open(filename, "r") as file:
        lines = file.readlines()

#Move 1st line (atom type) into the right position
    lines.insert(swap_pos, lines[0])
#Replace the original first line with the name of the POSCAR file
    lines[0] = "Image" + "0" + str(i) + "\n"

# Turn on selective dynamics, comment this out if not needed
    lines = selectiveDynamics(lines)

# Write the output
    lines = "".join(lines)
    with open(filename, "w") as file:
        file.write(lines)
