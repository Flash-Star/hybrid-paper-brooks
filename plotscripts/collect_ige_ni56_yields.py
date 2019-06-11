
import numpy as np

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

print "# realization	CO_IGE	CO_Ni56	CONe_IGE	CONe_Ni56"
for r in range(11,41):
	i = r-11
	print "%i\t%16.10e\t%16.10e\t%16.10e\t%16.10e"%(r,a[i],b[i],c[i],d[i])





