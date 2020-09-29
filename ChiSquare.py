import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.colors
from scipy.stats import norm
from scipy.stats import chisquare
fig, ax = plt.subplots()
from scipy.optimize import curve_fit
import math
from numpy import *
import matplotlib.cm as cm

Good = [7.40608936, 5.01682905] #65,76
Total = [10.6253099, 5.18659390] # 65,76
error65_150=2.76619064495
error76_150 = [3.27758534954, 18.0008245204]
errorTotal=[1000*0.0033743483766, 1000*0.00316337474164]#65,76

#W0220+0137: (6-5), (7-6)
#Linewidth = 100 km/s z=3.12
W0220_43 = 2.02 
error_43=0.28
co65_100=7.39210938
error65_100=2.84882699414
co76_100=3.22069297
error76_100=2.15428796722

#W0149 (Linewidth unknown): z=3.22
W0149_43=1.6
W0149_43_error=0.3
W0149_98=2.2
W0149_98_error=0.2

#W0410-0913 (Linewidth unknown):  z=3.63
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



#Expected
data = loadtxt("radex_extract_data1e18_z=3.12.txt", unpack="True", usecols=(1,2,3,4,5,6,7,8,9,10,11,12), comments="#")
F10_list = np.array(data[3,:])*W0149_43/np.array(data[6,:])
F21_list = np.array(data[4,:])*W0149_43/np.array(data[6,:])
F32_list = np.array(data[5,:])*W0149_43/np.array(data[6,:])
F43_list = np.array(data[6,:])*W0149_43/np.array(data[6,:])
F54_list = np.array(data[7,:])*W0149_43/np.array(data[6,:])
F65_list = np.array(data[8,:])*W0149_43/np.array(data[6,:])		#Line flux of the CO(6-5) line 
F76_list = np.array(data[9,:])*W0149_43/np.array(data[6,:])		#Line flux of the CO(7-6) line
F87_list = np.array(data[10,:])*W0149_43/np.array(data[6,:])
F98_list = np.array(data[11,:])*W0149_43/np.array(data[6,:])	


#filenbr = index + 1



m =  14
n = 50 
#Name of the file values are indexed starting from 1
n_H2=np.zeros(m) 
T_kin=np.zeros(n)

#filenbr = index + 1
for index in range (len(F76_list)+1): 
	if (index < m): 
		n_H2[index] = data[1,index] 
		n_H2[index] = np.log10(n_H2[index])
		#print n_H2
		#print index
		
	if (index%m == 0 and index!=0 and index <=len(F76_list)):
		T_kin[(index//m)-1] = data[0,index-m] 
		#print T_kin

		
			
	


#Assigning values to matrix
l_x2 = np.ones(shape=(len(n_H2),len(T_kin)))
j=0
i=0
k=0

#sigm=0.00214924900357
#JUpper= 5*1000*sigm
#yerror=np.array([error_43, error65_100, 0]) 
#v = np.array([W0220_43, co65_100, JUpper])
v = np.array([W0149_43, W0149_98])
yerror = np.array([W0149_43_error, W0149_98_error])
#v = np.array([W0410_10, W0410_43, W0410_65, W0410_76, W0410_98])
#v=np.array([W0410_65, W0410_76, W0410_98])
#[W0410_10_error, W0410_43_error, 
#yerror = np.array([W0410_10_error, W0410_43_error, W0410_65_error,W0410_76_error, W0410_98_error])
for index in range (len(F76_list)):
	if (index%m==0 and index!=0):
		j=j+1 
		i=0
	
	f_exp=np.array([F43_list[index-k], F98_list[index-k]])		
	#f_exp=np.array([F43_list[index], F65_list[index], F76_list[index]])
	reduced_chi_squared = 1.0/(9-2)*( (((f_exp[0]-v[0])/yerror[0])**2) + (((f_exp[1]-v[1])/yerror[1])**2))
	l_x2[i][j] = np.log10(reduced_chi_squared)
	i=i+1

	#elif(F76_list[index] > JUpper):
	#	l_x2[i][j] = np.nan
	#	i=i+1 
	#[F10_list[index], F43_list[index], , F98_list[index]
	#f_exp=np.array([F43_list[index],F65_list[index], F76_list[index]])
	#reduced_chi_squared = 1.0/(9-5)*sum(((f_exp-v)/yerror)**2) 
	#f_exp=np.array([F43_list[index-k], F98_list[index-k]])
	#f_exp=np.array([F10_list[index], F43_list[index], F65_list[index], F76_list[index], F98_list[index]])
	#if (np.log10(reduced_chi_squared) > 4.2):
	#	l_x2[i][j] = np.nan
	#	i=i+1
	#f_exp=np.array([F43_list[index-k], F65_list[index-k],F76_list[index-k]])
	#reduced_chi_squared = 1.0/(9-2)*( (((f_exp[0]-v[0])/yerror[0])**2) + (((f_exp[1]-v[1])/yerror[1])**2))

	
	
		#f_exp = np.array([F10_list[index-k], F43_list[index-k], F65_list[index-k], F76_list[index-k]])
		#f_exp = np.array([F43_list[index-k],F98_list[index-k]])
		#reduced_chi_squared = 1.0/(8-4)*( (((f_exp[0]-v[0])/yerror[0])**2) + (((f_exp[1]-v[1])/yerror[1])**2)+(((f_exp[2]-v[2])/yerror[2])**2) + (((f_exp[3]-v[3])/yerror[3])**2) )
		#reduced_chi_squared = 1.0/(9-3)*sum(((f_exp-v)/yerror)**2) 		
		
	#elif(F76_list[index] > JUpper):
	#		l_x2[i][j] = np.nan
	#		i=i+1
	#chi=chisquare([co65_100, co76_100],[F65_list[index-k],F76_list[index-k]])
	#chi=chisquare([Obs_43, co65_100, co76_100],[F43_list[index-k], F65_list[index-k],F76_list[index-k]], ddof=6)
	#chi=chisquare([ W0149_43, W0149_98 ], [ F43_list[index-k], F98_list[index-k] ])
	#chi=chisquare([W0410_10, W0410_43, W0410_65, W0410_76],[F10_list[index-k], F43_list[index-k], F65_list[index-k], F76_list[index-k]])
	#chi=chisquare([W0410_65, W0410_76, W0410_98],[F65_list[index-k], F76_list[index-k], F98_list[index-k]])
	#chi=chisquare([W0410_10, W0410_43, W0410_65],[F10_list[index-k], F43_list[index-k], F65_list[index-k]])
	#l_x2[i][j] = np.log10(chi[0]) 
	
		
			
		
			
		




plt.xticks(fontsize=15, weight='bold')
plt.yticks(fontsize=15, weight='bold')
#plt.title("Source of observation: ", size=20)

plt.ylabel(r'T$_{\rm kin}$ [K]',size=15, weight='bold')
plt.xlabel(r'log(n$_{\rm H_{2}}$) [cm$^{-3}$]',size=15, weight='bold')
#fig,ax=plt.subplots(figsize=(6,6))
mycmap = plt.get_cmap('gist_earth')



N=20 # Colorbarresolution: 20, 30, 50, 100
cf=plt.contourf(n_H2,T_kin,l_x2.T,N)



cb = fig.colorbar(cf)
cb.ax.tick_params(labelsize=16)
cb.ax.set_ylabel(r'log($\chi^2$)', size=15, weight='bold')
plt.show()

#fig.colorbar(cp)




















####################################################################################

#for i in range(len(F76_list)):
		#good_10[i] = np.abs(F10_list[i]-Judit_10)
	#good_10[i] = np.abs(F10_list[i]-W0410_10)
	#good_32[i] = np.abs(F32_list[i]-Judit_32)
	#good_43[i] = np.abs(F43_list[i]-W0149_43)
	#good_43[i] = np.abs(F43_list[i]-W0410_43)
	#good_54[i] = np.abs(F54_list[i]-Judit_54)
	#good_65[i] = np.abs(F65_list[i]-co65_100)
	#good_65[i] = np.abs(F65_list[i]-W0410_65)
	#good_76[i] = np.abs(F76_list[i]-co76_100)
	#good_76[i] = np.abs(F76_list[i]-W0410_76)
	#good_87[i] = np.abs(F87_list[i]-Judit_87)
	#good_98[i] = np.abs(F98_list[i]-W0149_98)
	#good_98[i] = np.abs(F98_list[i]-W0410_98)
	


#filenbr = index + 1
#for index in range (len(F76_list)+1): 
#	if (index < m): 
		
#		n_H2[index] = data2[1,index] 
#		n_H2[index] = np.log10(n_H2[index])
#		print n_H2
		#print index
		#print data2[2,index-1] #Current N_col
		
#	if (index%m == 0 and index!=0 and index <=len(F76_list)):
#		T_kin[(index//m)-1] = data2[0,index-m] 
		#print T_kin	



#for index in range (len(F76_list)):
		#filenbr = index + 1
#	if (index%m==0 and index!=0):
		#print index, j
#		j=j+1 
#		i=0
		#print index
	
#	l_x2[i][j] = np.log10(good_65[index-k]+good_76[index-k]+good_43[index-k])
#	i=i+1












####################################################################################








#filenbr = index + 1
#for index in range (len(F76_list)+1): 
#	if (index%m==0 and index!=0 index <= n): 
		#print index, n_H2
#		n_H2[(index//m)-1] = data2[1,index-m] 
#		n_H2[(index//m)-1] = np.log10(n_H2[(index//m)-1])
		
		#print data2[2,index-1] #Current N_col
		
#	if (index%n == 0 and index!=0 and index <=800):
#		T_kin[(index//n)-1] = data2[0,index-n] 
#		print T_kin, index 	
		#print data2[2,index-n] #Current N_col




#Assigning values to matrix
#l_x2 = np.zeros(shape=(len(n_H2),len(T_kin))) #24,768
#j=0
#i=0
#k=m
#for index in range (len(F76_list)):
#	if (index%m == 0 and index !=0): #filenbr = index + 1
		#print i,index
#		l_x2[i][j] = np.log10(good_65[index-k]+good_76[index-k]+good_43[index-k])
#		i=i+1
		
#	if ((index)%n==0 and index !=0):
#		j=j+1 
#		i=0





