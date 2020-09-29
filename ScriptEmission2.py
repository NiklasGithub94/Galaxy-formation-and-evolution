import math
import os
import sys
import numpy as np
from numpy import *

# ranges 
Tmin = 1
Tmax = 500 
Tstep = 10
logn_min = 1 #(1)
logn_max = 8 
logn_step = 0.5 #(0.2)











N = 1e+18
my_prefix = "radex_source_"
omega_s = 0.5**2  
linewidth = 100  # 100, 200, 400 km/s

##
##  Create radex input file(s)
##


f = open('radex_extract_data1e18_z=3.12.txt', 'w')
name=0


# Other important values
# lambda rest wavelength will be extracted from the data output files.  See the loop below. 
# In the loop, the T_R [K] from Radex is converted into flux density [mJy] using standard formulas


for T in arange(Tmin,Tmax,Tstep):
   for logn in arange(logn_min,logn_max,logn_step):
                name=name+1
                inputfile = my_prefix + str(name) + ".out"
                f.write(inputfile+' ')
                f.write(str(T)+' ')
                n = 10**logn
                f.write(str(n)+' ')
                f.write(str(N)+' ')
                data=loadtxt(inputfile, comments=["*","Calculation","LINE","(K)"],usecols=(8,11,12))
                wave=loadtxt(inputfile, comments=["*","Calculation","LINE","(K)"],usecols=(5,8))
               	wave[:,0] = wave[:,0] / 10000.  # to go from um to cm; given in restframe. 
                S_nu = data[:,0] * omega_s / (1.36 * wave[:,0]**2)   
                [f.write(str(j)+' ') for j in S_nu[:]]     # output is in mJy  (S_peak)

                [f.write(str(j)+' ') for j in data[:,0]]
                f.write('\n')

f.close()
