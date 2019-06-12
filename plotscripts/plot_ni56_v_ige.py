import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# From Rich Townsend for mesa3

params = {'backend': 'pdf',
 'figure.figsize': [3.38, 3.38],
 'font.family':'serif',
 'font.size':10,
 'font.serif': 'Times Roman',
 'axes.titlesize': 'medium' ,
 'axes.labelsize':'medium',
 'legend.fontsize':8,
 'legend.frameon':False,
 'text.usetex': True,
 'figure.dpi':600,
 'lines.markersize':4,
 'lines.linewidth':1,
 'lines.antialiased':False,
 'path.simplify':False,
 # Townsley below here
 'legend.numpoints': 1}

matplotlib.rcParams.update(params)

ORANGE = (0.90, 0.60, 0.00)
SKY_BLUE = (0.35, 0.70, 0.90)
BLUE_GREEN = (0.00, 0.60, 0.50)
YELLOW = (0.95, 0.90, 0.25)
BLUE = (0.00, 0.45, 0.70)
VERMILLION = (0.80, 0.40, 0.00)
RED_PURPLE = (0.80, 0.60, 0.70)

ax = plt.subplot(111)


#import data
data = np.genfromtxt("yields_ige_ni56.dat", names=True)

#CO
a = data['CO_IGE']
b = data['CO_Ni56']
plt.plot(a, b, "o", label ='CO', color = 'r', marker='s')

#HY
c = data['CONe_IGE']
d = data['CONe_Ni56']
plt.plot(c, d, "o", label ='CONe', color = 'b')


don_x = np.array( [0.8, 1.3] )
don_ni56_co = don_x*0.9251 - 0.0693

plt.plot( don_x, don_ni56_co, 'r--', label='W16 CO' )

don_ni56_hy = don_x*0.9368 - 0.0605

plt.plot( don_x, don_ni56_hy, 'b-', label='W16 CONe' )

plt.xlabel('IGE Yield (M$_\\odot$)')
plt.ylabel('$^{56}$Ni Yield (M$_\\odot$)')
plt.legend(loc='lower right')

ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

plt.tight_layout()
plt.savefig('ni56_v_ige.pdf')
#plt.show()



