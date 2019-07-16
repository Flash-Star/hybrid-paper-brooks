import matplotlib
import matplotlib.pyplot as plt
import numpy

fig, (axtop, axmid, axbot) = plt.subplots(3, 1, sharex=True, figsize=(3.38,5.0))
fig.subplots_adjust(hspace=0)

# From Rich Townsend for mesa3

params = {'backend': 'pdf',
# 'figure.figsize': [3.38, 3.38],
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


# file from /dmt/caugustine/Hybrid_Research/flash_research/wdbuilder/WDBuilder_SNIa-ddt/CO_WD_4km_cfbrooks_flash_pro12.dat
dc = numpy.genfromtxt( 'CO_WD_4km_cfbrooks_flash_pro12.dat',
	skip_header=2, names=('radius','density','temperature','c12','ne22') )

# file from /dmt/caugustine/Hybrid_Research/flash_runs/snia_10_hybrid2/400k_flash_21new.dat
dh = numpy.genfromtxt( '400k_flash_21new.dat',
	skip_header=2, names=('radius','density','temperature','c12','ne20','ne22') )

Rsun = 6.9598e10

axtop.semilogy(dc['radius']/1e8,dc['temperature'], color='black', linestyle='-', label='C--O')
axtop.semilogy( dh['radius']/1e8,dh['temperature'], color='black', linestyle='--', label='C--O--Ne')
axtop.legend(loc='best')
axtop.set_ylabel('Temperature (K)')
axtop.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

axmid.plot(dc['radius']/1e8,numpy.log10(dc['density']), 'k-', label='C--O')
axmid.plot( dh['radius']/1e8,numpy.log10(dh['density']), 'k--', label='C--O--Ne')
axmid.legend(loc='best')
axmid.set_ylim(-1.9,9.9)
axmid.set_ylabel('Log Density (g cm$^{-3}$)')
axmid.yaxis.set_label_coords(-0.12, 0.55)
axmid.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
axmid.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())



#axbot.semilogy(Rsun*10**dm['logR'],10**dm['log_he4'], color='black', linestyle='-', label='He4')
#axbot.semilogy( du['radius'],du['he4'], color='black', linestyle='--')

#axbot.semilogy(Rsun*10**dm['logR'],10**dm['log_n14'], 'g-', label='N14')
#axbot.semilogy( du['radius'],du['n14'], 'g--')

axbot.semilogy( dc['radius']/1e8,dc['c12'], '-', color=VERMILLION, label='$^{12}$C')
axbot.semilogy( dh['radius']/1e8,dh['c12'], '--', color=VERMILLION)

axbot.semilogy( dc['radius']/1e8,1.0-dc['c12']-dc['ne22'], '-', color='black', label='$^{16}$O')
axbot.semilogy( dh['radius']/1e8,1.0-dh['c12']-dh['ne20']-dh['ne22'], '--', color='black')

axbot.semilogy( dc['radius']/1e8,0.0*dc['ne22'], '-', color=BLUE, label='$^{20}$Ne')
axbot.semilogy( dh['radius']/1e8,dh['ne20'], '--', color=BLUE)

axbot.semilogy( dc['radius']/1e8,dc['ne22'], '-', color=BLUE_GREEN, label='$^{22}$Ne')
axbot.semilogy( dh['radius']/1e8,dh['ne22'], '--', color=BLUE_GREEN)

axbot.set_ylim(7e-4,1)

axbot.set_ylabel('Abundance (mass frac.)')
axbot.set_xlabel('Radius ($10^{8}$ cm)')

axbot.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

axbot.legend(loc='best')

#plt.tight_layout()
plt.savefig('temp_dens_abund_profile.pdf', bbox_inches='tight')
#plt.show()
