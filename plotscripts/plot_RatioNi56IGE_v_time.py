import matplotlib
import matplotlib.pyplot as plt
import numpy

matplotlib.rc_file("ubuntu_matplotlibrc")

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
          'figure.dpi': 600,
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

data21 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_21/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data22 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_22/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data23 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_23/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data24 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_24/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data25 = numpy.genfromtxt( '/dmt/townsley/mixed_hybrid_wd_snia/finish_runs/snia_25/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data26 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_26/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data27 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_27/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data28 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_28/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data29 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_29/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )
data30 = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_30/CO_WD_4km_cfbrooks_flash_2.dat', unpack=True )


data21HY = numpy.genfromtxt( '/dmt/townsley/mixed_hybrid_wd_snia/finish_runs/snia_21_hybrid2/profile21_flash_h201.dat', unpack=True )
data22HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_22_hybrid2/profile21_flash_h201.dat', unpack=True )
data23HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_23_hybrid2/profile21_flash_h201.dat', unpack=True )
data24HY = numpy.genfromtxt( '/dmt/townsley/mixed_hybrid_wd_snia/finish_runs/snia_24_hybrid2/profile21_flash_h201.dat', unpack=True )
data25HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_25_hybrid2/profile21_flash_h201.dat', unpack=True )
data26HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_26_hybrid2/profile21_flash_h201.dat', unpack=True )
data27HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_27_hybrid2/profile21_flash_h201.dat', unpack=True )
data28HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_28_hybrid2/profile21_flash_h201.dat', unpack=True )
data29HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_29_hybrid2/profile21_flash_h201.dat', unpack=True )
data30HY = numpy.genfromtxt( '/dmt/caugustine/Hybrid_Research/flash_runs/snia_30_hybrid2/profile21_flash_h201.dat', unpack=True )


mass21 = data21[15]/1.99e33
mass22 = data22[15]/1.99e33
mass23 = data23[15]/1.99e33
mass24 = data24[15]/1.99e33
mass25 = data25[15]/1.99e33
mass26 = data26[15]/1.99e33
mass27 = data27[15]/1.99e33
mass28 = data28[15]/1.99e33
mass29 = data29[15]/1.99e33
mass30 = data30[15]/1.99e33

IGE21= data21[13]/1.99e33
IGE22= data22[13]/1.99e33
IGE23= data23[13]/1.99e33
IGE24= data24[13]/1.99e33
IGE25= data25[13]/1.99e33
IGE26= data26[13]/1.99e33
IGE27= data27[13]/1.99e33
IGE28= data28[13]/1.99e33
IGE29= data29[13]/1.99e33
IGE30= data30[13]/1.99e33

mass21HY = data21HY[15]/1.99e33
mass22HY = data22HY[15]/1.99e33
mass23HY = data23HY[15]/1.99e33
mass24HY = data24HY[15]/1.99e33
mass25HY = data25HY[15]/1.99e33
mass26HY = data26HY[15]/1.99e33
mass27HY = data27HY[15]/1.99e33
mass28HY = data28HY[15]/1.99e33
mass29HY = data29HY[15]/1.99e33
mass30HY = data30HY[15]/1.99e33

IGE21HY = data21HY[13]/1.99e33
IGE22HY = data22HY[13]/1.99e33
IGE23HY = data23HY[13]/1.99e33
IGE24HY = data24HY[13]/1.99e33
IGE25HY = data25HY[13]/1.99e33
IGE26HY = data26HY[13]/1.99e33
IGE27HY = data27HY[13]/1.99e33
IGE28HY = data28HY[13]/1.99e33
IGE29HY = data29HY[13]/1.99e33
IGE30HY = data30HY[13]/1.99e33


plt.plot( data21[0], mass21/IGE21, color = 'r', label = 'CO' )
plt.plot( data22[0], mass22/IGE22, color = 'r')
plt.plot( data23[0], mass23/IGE23, color = 'r')
plt.plot( data24[0], mass24/IGE24, color = 'r')
plt.plot( data25[0], mass25/IGE25, color = 'r')
plt.plot( data26[0], mass26/IGE26, color = 'r')
plt.plot( data27[0], mass27/IGE27, color = 'r')
plt.plot( data28[0], mass28/IGE28, color = 'r')
plt.plot( data29[0], mass29/IGE29, color = 'r')
plt.plot( data30[0], mass30/IGE30, color = 'r')

plt.plot( data21HY[0], mass21HY/IGE21HY, color = 'b', label = 'CONe' )
plt.plot( data22HY[0], mass22HY/IGE22HY, color = 'b')
plt.plot( data23HY[0], mass23HY/IGE23HY, color = 'b')
plt.plot( data24HY[0], mass24HY/IGE24HY, color = 'b')
plt.plot( data25HY[0], mass25HY/IGE25HY, color = 'b')
plt.plot( data26HY[0], mass26HY/IGE26HY, color = 'b')
plt.plot( data27HY[0], mass27HY/IGE27HY, color = 'b')
plt.plot( data28HY[0], mass28HY/IGE28HY, color = 'b')
plt.plot( data29HY[0], mass29HY/IGE29HY, color = 'b')
plt.plot( data30HY[0], mass30HY/IGE30HY, color = 'b')


plt.ylabel('Ratio of $^{56}$N to IGE Yield')
plt.xlabel('Time (s)')

plt.xlim([0,4])

ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

plt.legend(loc="lower right")

plt.tight_layout()
plt.savefig('RatioNi56IGE_v_time_plot.pdf')
#plt.show()

