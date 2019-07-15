import matplotlib
import matplotlib.pyplot as plt
import numpy

matplotlib.rc_file("ubuntu_matplotlibrc")

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
          'path.simplify': False,
          # townsley below here
          'legend.numpoints': 1}

matplotlib.rcParams.update(params)

ORANGE     = (0.90,0.60,0.00)
SKY_BLUE   = (0.35,0.70,0.90)
BLUE_GREEN = (0.00,0.60,0.50)
YELLOW     = (0.95,0.90,0.25)
BLUE       = (0.00,0.45,0.70)
VERMILLION = (0.80,0.40,0.00)
RED_PURPLE = (0.80,0.60,0.70)

ax = plt.subplot(111)

data21 = numpy.genfromtxt( '/dmt/townsley/mixed_hybrid_wd_snia/finish_runs/snia_21_hybrid2/profile21_flash_h201.dat', unpack=True )
data22 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_22_hybrid2/profile21_flash_h201.dat', unpack=True )
data23 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_23_hybrid2/profile21_flash_h201.dat', unpack=True )
data24 = numpy.genfromtxt( '/dmt/townsley/mixed_hybrid_wd_snia/finish_runs/snia_24_hybrid2/profile21_flash_h201.dat', unpack=True )
data25 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_25_hybrid2/profile21_flash_h201.dat', unpack=True )
data26 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_26_hybrid2/profile21_flash_h201.dat', unpack=True )
data27 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_27_hybrid2/profile21_flash_h201.dat', unpack=True )
data28 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_28_hybrid2/profile21_flash_h201.dat', unpack=True )
data29 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_29_hybrid2/profile21_flash_h201.dat', unpack=True )
data30 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_30_hybrid2/profile21_flash_h201.dat', unpack=True )

plt.plot( data21[0], data21[15]/1.99e33, label = '21', color=ORANGE )
plt.plot( data22[0], data22[15]/1.99e33, label = '22', color=SKY_BLUE )
plt.plot( data23[0], data23[15]/1.99e33, label = '23', color=BLUE_GREEN )
plt.plot( data24[0], data24[15]/1.99e33, label = '24', color=YELLOW )
plt.plot( data25[0], data25[15]/1.99e33, label = '25', color=BLUE )
plt.plot( data26[0], data26[15]/1.99e33, label = '26', color=VERMILLION )
plt.plot( data27[0], data27[15]/1.99e33, label = '27', color=RED_PURPLE )
plt.plot( data28[0], data28[15]/1.99e33, label = '28', color='black' )
plt.plot( data29[0], data29[15]/1.99e33, '--', label = '29', color=ORANGE )
plt.plot( data30[0], data30[15]/1.99e33, '--', label = '30', color=SKY_BLUE )


plt.xlabel('Time (s)')
plt.ylabel('Expected $^{56}$Ni Yield (M$_\\odot$)')
plt.legend(loc = 'best')

plt.xlim([0,4])

ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

plt.annotate("CONe Hybrid", (2.0,0.2))

plt.tight_layout()
plt.savefig('Hybrid_Ni56mass_v_time_plot.pdf')
#plt.show()
