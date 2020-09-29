import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
fig, ax = plt.subplots()
from scipy.optimize import curve_fit
import math


# Task 1: Apply Curve (and handmade) fit to reduction data 

arr = np.loadtxt('co65good_100_baselineremoved.dat') 

temp=arr[:,1]
vel=-arr[:,0]
x = vel[28:49]
Jy = 38*temp[28:49] #38* (mJy)


#matplotlib.rc('font', labelsize=20)
font = {'family' : 'normal',
		'weight' : 'bold',
		'size' : 20}

matplotlib.rc('font', **font)

plt.fill_between(x, (Jy*1000), step="pre", alpha=0.6, color='yellow')
plt.plot(x,np.abs(Jy),drawstyle="steps")
# #Plots step function spectrum from class data

 

'''

#What is this value? np.std(Jy)
n = len(x)		 
mean = sum(x * Jy)/n
sigm = sum(Jy*((x - mean)**2))/n
mean = 0
for i in range(0,len(Jy)):
	mean = mean + Jy[i]

mean = mean/sum(Jy)
s=np.zeros(len(Jy))

for j in range(0,len(Jy)):
	s[j] = s[j] + math.pow(s[j]-mean,2)
	s[j] = math.sqrt(s[j])/n	


sigm = sum(s)	
'''

def gaus(x0,a,mu,sigma):
	return a*np.exp(-(x0-mu)**2/(2*sigma**2))	



#p0 = [max(Jy),mean,sigm]

p0=[0.001,0,250]
popt,pcov = curve_fit(gaus,x,Jy,p0)

print popt
print np.sqrt(pcov[0,0]), 
#np.sqrt(pcov[1,1]), np.sqrt(pcov[2,2])

#ax.set_color_cycle(['blue'])
#plt.plot(x, gaus(x, *p0) ,label="Fit")
#plt.plot(x,np.zeros(len(x)),'--',label = '0')
ax.set_color_cycle(['black'])
plt.xlabel(r'Vel. [km/s]', fontsize='20', weight='bold')
ax.tick_params(axis="y", labelsize=20)
plt.ylabel(r'Flux density [mJy]',fontsize='20', weight='bold')
plt.plot(x, gaus(x, popt[0], popt[1], popt[2])*1000,lw=2, label='Curvefit')
plt.legend()
plt.show()


# Integral (summation over stepfunction in given interval, not Gaussian)
#x1=vel
#I=0
#for i in range(0, len(Jy)):
#	I = I + Jy[i]*(x1[i+1]-x1[i])

#1.9545
# I = 1.065*max(temp)*38*FWHM => 
#print "I_CO = ", I
#FWHM = I/(max(temp)*38*1.065) 
#print "FWHM= ", FWHM
#std = rms = , line = rms*sqrt(nbr of channels) = (nbr of channels = 21)
#standard_deviation = FWHM/(2.355) 
#line = standard_deviation*np.sqrt(21)
#print "rms =", standard_deviation
#print "line =", line




#####################################################################
#We find FWHM using code for the real data and Gaussian fit

# Real data
#y = temp
#max_y = max(y*38)  # Find the maximum y value (Temp)
#xs = [x for x in range(len(y)) if y[x]*38 > 38*max_y/2.0]
#print min(xs), max(xs) # Print the points at half-maximum ,
#print y[min(xs)]*38, y[max(xs)]*38
#print vel[26+min(xs)], vel[26+max(xs)]


#Gaussian data
#x = np.linspace(-600, 600, len(y1))
 
#y1=gaus(x,*p0)*38 #Gaussian fit in interval -600, 600
#max_y1 = max(y1)  # Find the maximum value in Gaussian fit
#xs = [x for x in range(len(y1)) if (y1[x]*38) > (38*max_y1/2.0)]





#######################################################################



#def IntegrateGauss(var,amplitude,mu,sig,a,b,N):
#	def f(x):
#		amplitude*np.exp(-(x-mu)**2/(sig**2))
#	return amplitude*np.exp(-(x-mu)**2/(sig**2))
#
#	var = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
 #   	fx = f(var)
	#area = np.sum(fx)*(b-a)/N
#	return area
	



