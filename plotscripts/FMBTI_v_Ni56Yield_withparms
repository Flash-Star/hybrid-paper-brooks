import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# From Rich Townsend for mesa3

params = {'backend': 'pdf',
 'figure.figsize': [3.38, 3.38],
 'font.family':'serif',
 'font.size':10,
# 'font.serif': 'Times Roman',
 'axes.titlesize': 'medium' ,
 'axes.labelsize':'medium',
 'legend.fontsize':8,
 'legend.frameon':False,
# 'text.usetex': True,
# 'figure.dpi':600,
 'lines.markersize':4,
 'lines.linewidth':1,
 'lines.antialiased':False,
 'path.simplify':False}

matplotlib.rcParams.update(params)

ORANGE = (0.90, 0.60, 0.00)
SKY_BLUE = (0.35, 0.70, 0.90)
BLUE_GREEN = (0.00, 0.60, 0.50)
YELLOW = (0.95, 0.90, 0.25)
BLUE = (0.00, 0.45, 0.70)
VERMILLION = (0.80, 0.40, 0.00)
RED_PURPLE = (0.80, 0.60, 0.70)


#import integral file
filelistCO = []
filelistHY = []
for i in range(11,41):
    filelistCO.append("/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_%s/CO_WD_4km_cfbrooks_flash_2.dat" %i)

for i in range(11,41):
    filelistHY.append("/dmt/caugustine/Hybrid_Research/flash_runs/snia_%s_hybrid2/profile21_flash_h201.dat" %i)

#CO
gpermsun = 1.988435e33
a = []
b = []
for fname in filelistCO:
	data = np.loadtxt(fname)
	x = data[-1][13]
	xsolar = x/gpermsun
	a.append(xsolar)
	y = data[-1][15]
	ysolar = y/gpermsun
	b.append(ysolar)
print(a)
print(b)
plt.plot(a, b, "o", label ='CO', color = 'b')

#HY
gpermsun = 1.988435e33
c = []
d = []
for fname in filelistHY:
	data = np.loadtxt(fname)
	x = data[-1][13]
	xsolar = x/gpermsun
	c.append(xsolar)
	y = data[-1][15]
	ysolar = y/gpermsun
	d.append(ysolar)
print(c)
print(d)
plt.plot(c, d, "o", label ='CO', color = 'r')

plt.xlabel('Final Mass Burned to IGE (M$_\\odot$)')
plt.ylabel('Estimated Ni56 Yield (M$_\\odot$)')
plt.tight_layout()
plt.savefig('FMBI_v_Ni56Yield_plot.pdf')
#plt.show()



