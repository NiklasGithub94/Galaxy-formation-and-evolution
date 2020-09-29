import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm
from scipy.stats import chisquare
from scipy.interpolate import interp1d
fig, ax = plt.subplots()
from scipy.optimize import curve_fit
import math
from numpy import *

#Print 

#W0220+0137: z=3.12
#Linewidth = 100 km/s, mJy
W0220_43 = 2.02 #CO(4-3) transition
W0220_43_error=0.28
W0220_65=7.39210938 #CO(6-5)
W0220_65_error=2.84882699414
W0220_76=3.22069297 #CO(7-6)
error76_100=2.15428796722
sigm=0.00214924900357
JUpper= 3*1000*sigm #3sigma and 5sigma, Jy -> mJy

#Calculated by Radex (Software)
data = np.loadtxt("radex_extract_data1e18_z=3.12.txt", unpack="True", usecols=(1,2,3,4,5,6,7,8,9,10,11,12), comments="#")
F10_list = np.array(data[3,:])*(W0220_43)/np.array(data[6,:])
F21_list = np.array(data[4,:])*(W0220_43)/np.array(data[6,:])
F32_list = np.array(data[5,:])*(W0220_43)/np.array(data[6,:])
F43_list = np.array(data[6,:])*(W0220_43)/np.array(data[6,:])
F54_list = np.array(data[7,:])*(W0220_43)/np.array(data[6,:])	
F65_list = np.array(data[8,:])*(W0220_43)/np.array(data[6,:])	#Line flux of the CO(6-5) line, normalise to CO(6-5), relative comparison
F76_list = np.array(data[9,:])*(W0220_43)/np.array(data[6,:])	#Line flux of the CO(7-6) line 
F87_list = np.array(data[10,:])*(W0220_43)/np.array(data[6,:])	
F98_list = np.array(data[11,:])*(W0220_43)/np.array(data[6,:])

#Plot x-axis, all transitions, independently of input
new_length=100
JJ=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
fake=[1,10]
x_ticks=[0.1,0.2,0.3,0.4, 0.5,0.6,0.7,0.8,0.9]
my_xticks = ['CO(1-0)','CO(2-1)','CO(3-2)', 'CO(4-3)', 'CO(5-4)', 'CO(6-5)', 'CO(7-6)', 'CO(8-7)', 'CO(9-8)']
plt.errorbar([JJ[0],JJ[8]],fake,xerr=[0.1,0.1],fmt='',color='white')


v = np.array([W0220_43, W0220_65, W0220_76])
yerror = np.array([W0220_43_error,W0220_65_error, 0])

plt.xticks(x_ticks, my_xticks, fontsize='20')
plt.errorbar( [x_ticks[3], x_ticks[5], x_ticks[6]], v, yerr = yerror , fmt='bs', label = 'Obs Data' , color='green' , markersize='20', ecolor='red',capsize=4, elinewidth=3)
for index in range(0, (len(data[0,:])-1)):
	
	f_exp=np.array([F43_list[index], F65_list[index], F76_list[index]])
	if(F76_list[index] < JUpper):
		reduced_chi_squared = 1.0/(9-2)*( (((f_exp[0]-v[0])/yerror[0])**2) + (((f_exp[1]-v[1])/yerror[1])**2))
	if(np.log10(reduced_chi_squared) < -1.15): #Suitable threshold
			print index 
			F10=F10_list[index]
			F21=F21_list[index]
			F32=F32_list[index]
			F43=F43_list[index]
			F54=F54_list[index]
			F65=F65_list[index]
			F76=F76_list[index]
			F87=F87_list[index]
			F98=F98_list[index]
			F=[F10,F21,F32,F43,F54,F65,F76,F87,F98]
			plt.errorbar(x_ticks, F, fmt='o', label='$T_{kin}$=' + str(data[0,index]) + ', $n_{H_{2}}$=' + str(round(data[1,index],2)) + ', log$(\chi^2)$='+ str(round(np.log10(reduced_chi_squared),2)))




plt.rc('legend',fontsize=20)
plt.xlabel(r'CO J-transition', fontsize='20', weight='bold')
ax.tick_params(axis="y", labelsize=20)
plt.ylabel(r'Peak flux density [mJy]',fontsize='20', weight='bold')
ax.legend(loc='upper left', frameon='False')
plt.show()
