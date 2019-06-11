import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

params = {'backend': 'pdf',
          'figure.figsize': [3.38, 3.38],
          'font.family':'serif',
          'font.size':10,
          'font.serif': 'Times Roman',
          'axes.titlesize': 'medium',
          'axes.labelsize': 'medium',
          'legend.fontsize': 8,
          'legend.frameon' : False,
          'text.usetex': True,
          'figure.dpi': 600,
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

ax = plt.subplot(111)


#import data
data = np.genfromtxt("yields_ige_ni56.dat", names=True)

#Hybrid Models
a = data['CONe_Ni56']

a.sort()                       # sort numbers in order
print(a)
totalnumber = len(a)           #find the length of the array: total number
print(totalnumber)
index = np.arange(1,totalnumber+1)
y = index/float(totalnumber)
plt.step(a, y, label = 'Hybrid', color = 'b', where='post')


#CO
a = data['CO_Ni56']

a.sort()                       # sort numbers in order
print(a)
totalnumber = len(a)           #find the length of the array: total number
print(totalnumber)
index = np.arange(1,totalnumber+1)
y = index/float(totalnumber)
plt.step(a, y, label = 'CO', color = 'r', linestyle=':', where='post')





#    Hybriddata = np.loadtxt(fname)
#    x = Hybriddata[len(data)-1,15]
#    totalnumber = 10
#    indexx =  a.index(xsolar)
#    y = indexx/totalnumber
#    xsolar = x/gpermsun
#    a.append(xsolar)

plt.legend(loc='best')
#plt.title('Cumulative distribution of estimated Ni56 Yield')
plt.xlabel('$^{56}$Ni Yield (M$_\\odot$)')
plt.ylabel('Cumulative Distribution')
plt.tight_layout()
ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.1))
plt.savefig('cum_dis_Ni56.pdf')
#plt.show()
             
