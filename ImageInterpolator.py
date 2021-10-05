# Last updated: 2020/8/10
# Written by Mark Ma

# The program is used to generate NEB images using ASE
# ===============================================

from ase.io.vasp import read_vasp
import os

from ase.io import write
from ase.io.vasp import read_vasp
from ase.neb import NEB

n_im = 2
# Read initial and final states:
initial = read_vasp('POSCAR1.VASP')
final = read_vasp('POSCAR2.VASP')
# Make a band consisting of 10 images:
images = [initial]
images += [initial.copy() for i in range(n_im)]
images += [final]
neb = NEB(images)
# Interpolate linearly the potisions of the 8 middle images:
neb.interpolate('idpp')
# Set calculators:
#for image in images[1:8]:
#    image.calc = Vasp2(...)

# Optimize:
#optimizer = MDMin(neb, trajectory='A2B.traj')
#optimizer.run(fmax=0.04)
for i in range(len(images)):
    os.system("mkdir %02i" % i) #makes folder 00, 01, 02
    write("%02i/POSCAR" % i,neb.images[i],format="vasp")





