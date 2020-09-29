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



#W0220+0137: z=3.12
#Linewidth = 100 km/s
W0220_43 = 2.02
W0220_43_error=0.28
W0220_65=7.39210938 #mJy
W0220_65_error=2.84882699414
W0220_76=3.22069297 #mJy
error76_100=2.15428796722
sigm=0.00214924900357
JUpper= 3*1000*sigm #3sigma and 5sigma

#W0149 (Linewidth unknown): z=3.22
W0149_43=1.6
W0149_43_error=0.3
W0149_98=2.2
W0149_98_error=0.2

#W0410-0913 (Linewidth unknown): z=3.59
W0410_10 = 0.272
W0410_10_error=0.056
W0410_43=5.2
W0410_43_error=0.536
W0410_65=6.4
W0410_65_error=0.32
W0410_76=7.2
W0410_76_error=0.64
W0410_98=5.2
W0410_98_error=0.4

#Expected (Radex)
data = np.loadtxt("radex_extract_data1e18_z=3.12.txt", unpack="True", usecols=(1,2,3,4,5,6,7,8,9,10,11,12), comments="#")
F10_list = np.array(data[3,:])*(W0220_43)/np.array(data[6,:])
F21_list = np.array(data[4,:])*(W0220_43)/np.array(data[6,:])
F32_list = np.array(data[5,:])*(W0220_43)/np.array(data[6,:])
F43_list = np.array(data[6,:])*(W0220_43)/np.array(data[6,:])
F54_list = np.array(data[7,:])*(W0220_43)/np.array(data[6,:])	
F65_list = np.array(data[8,:])*(W0220_43)/np.array(data[6,:])	#Line flux of the CO(6-5) line 
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
#yerror=np.array([W0220_43_error,W0220_65_error, error76_100])
#v = np.array([W0220_43, W0220_65, JUpper])
yerror = np.array([W0220_43_error,W0220_65_error, 0])

#v = np.array([W0149_43, W0149_98])
#yerror = np.array([W0149_43_error, W0149_98_error])


#v = np.array([W0410_10, W0410_43, W0410_65,W0410_76, W0410_98]) 
#v = np.array([W0410_65, W0410_76, W0410_98])
#W0410_76, W0410_98]
#yerror = np.array([W0410_10_error, W0410_43_error, W0410_65_error, W0410_76_error, W0410_98_error])
#yerror = np.array([W0410_65_error, W0410_76_error, W0410_98_error])
#W0410_76_error, W0410_98_error] 

#v= [W0410_65, W0410_76]

plt.xticks(x_ticks, my_xticks, fontsize='20')
plt.errorbar( [x_ticks[3], x_ticks[5], x_ticks[6]], v, yerr = yerror , fmt='bs', label = 'Obs Data' , color='green' , markersize='20', ecolor='red',capsize=4, elinewidth=3)

#[x_ticks[3], x_ticks[5], x_ticks[6]]
# #[x_ticks[3], x_ticks[8]]
#[x_ticks[0], x_ticks[3],x_ticks[5], x_ticks[6],x_ticks[8]]

#arrow = u'$\u2193$
for index in range(0, (len(data[0,:])-1)):
	
	f_exp=np.array([F43_list[index], F65_list[index], F76_list[index]])
	#f_exp=np.array([F10_list[index], F43_list[index], F65_list[index], F76_list[index], F98_list[index]]) 
	#F76_list[index], F98_list[index]])
	#f_exp=np.array([F65_list[index],F76_list[index], F98_list[index]])
	#f_exp=np.array([F43_list[index], F98_list[index]])
	#reduced_chi_squared = 1.0/(9-3)*sum(((f_exp-v)/yerror)**2) 
	
	if(F76_list[index] < JUpper):
		reduced_chi_squared = 1.0/(9-2)*( (((f_exp[0]-v[0])/yerror[0])**2) + (((f_exp[1]-v[1])/yerror[1])**2))
	if(np.log10(reduced_chi_squared) < -1.15):
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
			#new_x = np.linspace(0.1, 0.9, new_length)
			#new_y = sp.interpolate.interp1d(x_ticks, F, kind='cubic')(new_x)
			#plt.plot(new_x, new_y)




plt.rc('legend',fontsize=20)
plt.xlabel(r'CO J-transition', fontsize='20', weight='bold')
ax.tick_params(axis="y", labelsize=20)
plt.ylabel(r'Peak flux density [mJy]',fontsize='20', weight='bold')
ax.legend(loc='upper left', frameon='False')
plt.show()




############################################################################################

#for i in range(0, (len(data[0,:])-1)):
	#good_10[i] = np.abs(F10_list[i]-Judit_10)
	#good_10[i] = np.abs(F10_list[i]-W0410_10)
	#good_43[i] = np.abs(F43_list[i]-W0149_43)
	#good_43[i] = np.abs(F43_list[i]-W0410_43)
	#good_65[i] = np.abs(F65_list[i]-W0220_65)
	#good_65[i] = np.abs(F65_list[i]-W0410_65)
	#good_76[i] = np.abs(F76_list[i]-W0220_76)
	#good_76[i] = np.abs(F76_list[i]-W0410_76)
	#good_98[i] = np.abs(F98_list[i]-W0149_98)
	#good_98[i] = np.abs(F98_list[i]-W0410_98)	

#if( ((good_10[index]**2)/(F10_list[index])+(good_43[index]**2)/(F43_list[index])+(good_65[index]**2)/(F65_list[index]) )<0.6):
#+ (good_76[index]**2)/(F76_list[index]) + (good_98[index])**2/(F98_list[index]) ) < 10):

