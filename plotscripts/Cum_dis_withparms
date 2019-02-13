import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

params = {'backend': 'pdf',
          'figure.figsize': [3.38, 3.38],
          'font.family':'serif',
          'font.size':10,
#          'font.serif': 'Times Roman',
          'axes.titlesize': 'medium',
          'axes.labelsize': 'medium',
          'legend.fontsize': 8,
          'legend.frameon' : False,
#          'text.usetex': True,
#          'figure.dpi': 600,
          'lines.markersize': 4,
          'lines.linewidth': 1,
          'lines.antialiased': False,
          'path.simplify': False }

matplotlib.rcParams.update(params)

ORANGE     = (0.90,0.60,0.00)
SKY_BLUE   = (0.35,0.70,0.90)
BLUE_GREEN = (0.00,0.60,0.50)
YELLOW     = (0.95,0.90,0.25)
BLUE       = (0.00,0.45,0.70)
VERMILLION = (0.80,0.40,0.00)
RED_PURPLE = (0.80,0.60,0.70)

#import integral file
filelistCO = []
filelistHY = []
for i in range(11,41):
    filelistCO.append("/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_%s/CO_WD_4km_cfbrooks_flash_2.dat" %i)

for i in range(11,41):
    filelistHY.append("/dmt/caugustine/Hybrid_Research/flash_runs/snia_%s_hybrid2/profile21_flash_h201.dat" %i)

#plot Ni-56 mass profile
gpermsun = 1.988435e33 # grams/Msun
a = []
for fname in filelistCO:
    print(fname)
    data = np.loadtxt(fname)
    x = data[-1][15]   #final estimated mass
    xsolar = x/gpermsun        #convert to solar mass
    a.append(xsolar)           # add to array
    print(xsolar)

a.sort()                       # sort numbers in order
print(a)
totalnumber = len(a)           #find the length of the array: total number
print(totalnumber)
index = np.arange(1,totalnumber+1)
y = index/float(totalnumber)
plt.plot(a, y, label = 'CO', color = 'b')

#Hybrid Models
gpermsun = 1.988435e33 # grams/Msun
a = [] 
for fname in filelistHY:
    print(fname)
    data = np.loadtxt(fname)
    x = data[-1][15]   #final estimated mass
    xsolar = x/gpermsun        #convert to solar mass
    a.append(xsolar)           # add to array
    print(xsolar)

a.sort()                       # sort numbers in order
print(a)
totalnumber = len(a)           #find the length of the array: total number
print(totalnumber)
index = np.arange(1,totalnumber+1)
y = index/float(totalnumber)
plt.plot(a, y, label = 'Hybrid', color = 'r')






#    Hybriddata = np.loadtxt(fname)
#    x = Hybriddata[len(data)-1,15]
#    totalnumber = 10
#    indexx =  a.index(xsolar)
#    y = indexx/totalnumber
#    xsolar = x/gpermsun
#    a.append(xsolar)

plt.legend(loc='best')
#plt.title('Cumulative distribution of estimated Ni56 Yield')
plt.xlabel('Estimated Ni56 Yield (M$_\\odot$)')
plt.ylabel('Cumulative Fraction')
plt.tight_layout()
plt.savefig('Cum_dis_Ni56mass_plot.pdf')
#plt.show()
             
