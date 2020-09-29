import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
fig, ax = plt.subplots()
from scipy.optimize import curve_fit
import math


# Apply fit to reduction data 

arr = np.loadtxt('co65good_100_baselineremoved.dat') #100 km/s linewidth

temp=arr[:,1] #Temperature [K]
vel=-arr[:,0] #Velocity [km/s] switch sign due to data, 
x = vel[28:49] #Select interesting interval
Jy = 38*temp[28:49] # Conversion factor: 38 (Jy/K)

font = {'family' : 'normal',
		'weight' : 'bold',
		'size' : 20}

matplotlib.rc('font', **font)

plt.fill_between(x, (Jy*1000), step="pre", alpha=0.6, color='yellow')
plt.plot(x,np.abs(Jy),drawstyle="steps")
#Plots step function spectrum from class data

 
#Function: Fit data to Gaussian function
def gaus(x0,a,mu,sigma):
	return a*np.exp(-(x0-mu)**2/(2*sigma**2))	




p0=[0.001,0,250] #Initial guess
popt,pcov = curve_fit(gaus,x,Jy,p0) #Best fit

print popt #Optimal value/fit
print np.sqrt(pcov[0,0]) #Square root covariance
ax.set_color_cycle(['black'])
plt.xlabel(r'Vel. [km/s]', fontsize='20', weight='bold')
ax.tick_params(axis="y", labelsize=20)
plt.ylabel(r'Flux density [mJy]',fontsize='20', weight='bold')
plt.plot(x, gaus(x, popt[0], popt[1], popt[2])*1000,lw=2, label='Curvefit')
plt.legend()
plt.show()
