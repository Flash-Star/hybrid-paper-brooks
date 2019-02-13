import matplotlib
import matplotlib.pyplot as plt
import numpy

# from Rich Townsend for mesa3
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


data21 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_21/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data22 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_22/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data23 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_23/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data24 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_24/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data25 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_25/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data26 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_26/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data27 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_27/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data28 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_28/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data29 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_29/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data30 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_30/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )

plt.plot( data21[0], data21[15]/1.99e33, label = '21' )
plt.plot( data22[0], data22[15]/1.99e33, label = '22' )
plt.plot( data23[0], data23[15]/1.99e33, label = '23' )
plt.plot( data24[0], data24[15]/1.99e33, label = '24' )
plt.plot( data25[0], data25[15]/1.99e33, label = '25' )
plt.plot( data26[0], data26[15]/1.99e33, label = '26' )
plt.plot( data27[0], data27[15]/1.99e33, label = '27' )
plt.plot( data28[0], data28[15]/1.99e33, label = '28' )
plt.plot( data29[0], data29[15]/1.99e33, label = '29' )
plt.plot( data30[0], data30[15]/1.99e33, label = '30' )

plt.ylabel('Estimated Ni56 Mass (M$_\\odot$)')
plt.xlabel('Time(s)')

plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('CO_Ni56mass_v_time_plot.pdf')
#plt.show()

