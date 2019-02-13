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

#CO

data25 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_25/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data26 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_26/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data27 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_27/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data28 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_28/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data29 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_29/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data30 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_30/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )

plt.plot( data25[0], data25[13]/1.99e33, color = 'blue')
plt.plot( data26[0], data26[13]/1.99e33, color = 'blue')
plt.plot( data27[0], data27[13]/1.99e33, color = 'blue')
plt.plot( data28[0], data28[13]/1.99e33, color = 'blue')
plt.plot( data29[0], data29[13]/1.99e33, color = 'blue')
plt.plot( data30[0], data30[13]/1.99e33, color = 'blue')
#HY

data25HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_25_hybrid2/profile21_flash_h201.dat', unpack=True )
data26HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_26_hybrid2/profile21_flash_h201.dat', unpack=True )
data27HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_27_hybrid2/profile21_flash_h201.dat', unpack=True )
data28HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_28_hybrid2/profile21_flash_h201.dat', unpack=True )
data29HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_29_hybrid2/profile21_flash_h201.dat', unpack=True )
data30HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_30_hybrid2/profile21_flash_h201.dat', unpack=True )

plt.plot( data25HY[0], data25HY[13]/1.99e33, color = 'red' )
plt.plot( data26HY[0], data26HY[13]/1.99e33, color = 'red' )
plt.plot( data27HY[0], data27HY[13]/1.99e33, color = 'red' )
plt.plot( data28HY[0], data28HY[13]/1.99e33, color = 'red')
plt.plot( data29HY[0], data29HY[13]/1.99e33, color = 'red')
plt.plot( data30HY[0], data30HY[13]/1.99e33, color = 'red')

plt.xlabel('Time (s)')
plt.ylabel('Mass Burned to IGE (M$_\\odot$)')
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('MBTI_v_time_plot.pdf')
#plt.show()
