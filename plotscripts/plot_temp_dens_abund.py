import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy

dc = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_research/wdbuilder/WDBuilder_SNIa-ddt/CO_WD_4km_cfbrooks_flash_pro12.dat',
	skip_header=2, names=('radius','density','temperature','c12','ne22') )

dh = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_10_hybrid2/400k_flash_21new.dat',
	skip_header=2, names=('radius','density','temperature','c12','ne20','ne22') )

fig, (axtop, axbot) = plt.subplots(nrows=2)

axtop2 = axtop.twinx()

Rsun = 6.9598e10

axtop.semilogy(dc['radius'],dc['temperature'], color='black', linestyle='-', label='T')
axtop.semilogy( dh['radius'],dh['temperature'], color='black', linestyle='--', label='hybrid')

axtop2.semilogy(dc['radius'],dc['density'], 'r-', label='dens')
axtop2.semilogy( dh['radius'],dh['density'], 'r--')

axtop.legend(loc='best')
axtop2.legend(loc='best')


#axbot.semilogy(Rsun*10**dm['logR'],10**dm['log_he4'], color='black', linestyle='-', label='He4')
#axbot.semilogy( du['radius'],du['he4'], color='black', linestyle='--')

#axbot.semilogy(Rsun*10**dm['logR'],10**dm['log_n14'], 'g-', label='N14')
#axbot.semilogy( du['radius'],du['n14'], 'g--')

axbot.semilogy(dc['radius'],dc['c12'], 'r-', label='C12')
axbot.semilogy( dh['radius'],dh['c12'], 'r--')

axbot.semilogy( dc['radius'],1.0-dc['c12']-dc['ne22'], 'c-', label='O16')
axbot.semilogy( dh['radius'],1.0-dh['c12']-dh['ne20']-dh['ne22'], 'c--')

axbot.semilogy( dc['radius'],0.0*dc['ne22'], 'g-', label='Ne20')
axbot.semilogy( dh['radius'],dh['ne20'], 'g--')

axbot.semilogy( dc['radius'],dc['ne22'], 'b-', label='Ne22')
axbot.semilogy( dh['radius'],dh['ne22'], 'b--'  )

axbot.set_ylim(1e-4,1)

axbot.legend(loc='best')

plt.show()
