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



N = 1e+18 #(14) 15, 16, 17 (18)
my_prefix = "radex_source_"
omega_s = 0.5**2  
linewidth = 100  #100, 200, 400 km/s

##
##  Create radex input file(s)
##

my_inputfile = "radex1e18_z=3.12.inp"
f = open('radex1e18_z=3.12.inp','w')
name=0
#Printed to radex input file, radex.inp
for T in arange(Tmin,Tmax,Tstep):
    for logn in arange(logn_min,logn_max,logn_step):
                name=name+1
                f.write("co.dat"+'\n')
                f.write(my_prefix + str(name) + ".out"+'\n')
                f.write("100 1100"+'\n') #Frequency range
                f.write(str(T)+'\n')
                f.write(str(1)+'\n')
                f.write("H2"+'\n')
                n = 10**logn
                f.write(str(n)+'\n')
                f.write(str(11.25)+'\n') #z=3.12,T=11.25  z=3.22,T=11.5  z=3.63,T=12.63
                f.write(str(N)+'\n')
                f.write(str(linewidth)+'\n')
                f.write(str(1)+'\n')
              	
            


f.close()            
os.system("radex < "+my_inputfile) #Run Radex on radex.inp
             
