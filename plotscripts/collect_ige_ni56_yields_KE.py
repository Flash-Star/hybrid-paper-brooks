
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
CO_KE = []
for fname in filelistCO:
	data = np.loadtxt(fname)
	x = data[-1][13]
	xsolar = x/gpermsun
	a.append(xsolar)
	y = data[-1][15]
	ysolar = y/gpermsun
	b.append(ysolar)
	# ener + e_grav
	CO_KE.append(data[-1][5]+data[-1][8])

#HY
gpermsun = 1.988435e33
c = []
d = []
CONe_KE = []
for fname in filelistHY:
	data = np.loadtxt(fname)
	x = data[-1][13]
	xsolar = x/gpermsun
	c.append(xsolar)
	y = data[-1][15]
	ysolar = y/gpermsun
	d.append(ysolar)
	# ener + e_grav
	CONe_KE.append(data[-1][5]+data[-1][8])

print "# realization	CO_IGE	CO_Ni56	CONe_IGE	CONe_Ni56	CO_KE	CONe_KE"
for r in range(11,41):
	i = r-11
	print "%i\t%16.10e\t%16.10e\t%16.10e\t%16.10e\t%16.10e\t%16.10e"%(r,a[i],b[i],c[i],d[i],CO_KE[i],CONe_KE[i])

# print averages and standard dev
print "# Averages +/- standard deviations, Msun or ergs"
print "#  CO   IGE : %16.10e +/- %16.10e"%(np.mean(a),np.std(a,ddof=1))
print "#  CO   Ni56: %16.10e +/- %16.10e"%(np.mean(b),np.std(b,ddof=1))
print "#  CONe IGE : %16.10e +/- %16.10e"%(np.mean(c),np.std(c,ddof=1))
print "#  CONe Ni56: %16.10e +/- %16.10e"%(np.mean(d),np.std(d,ddof=1))
print "#  CO   KE  : %16.10e +/- %16.10e"%(np.mean(CO_KE),np.std(CO_KE,ddof=1))
print "#  CONe KE  : %16.10e +/- %16.10e"%(np.mean(CONe_KE),np.std(CONe_KE,ddof=1))





