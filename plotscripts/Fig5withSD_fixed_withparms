import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

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
#         'text.usetex': True,
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



#import integral file
filelistCO = []
filelistHY = []
for i in range(11,41):
    filelistCO.append("/dmt/caugustine/Hybrid_Research/flash_runs_CO/snia_%s/CO_WD_4km_cfbrooks_flash_2.dat" %i)

for i in range(11,41):
    filelistHY.append("/dmt/caugustine/Hybrid_Research/flash_runs/snia_%s_hybrid2/profile21_flash_h201.dat" %i)


CO_Mass_ddt =[ 2.17181312005e+33, 2.35383629797e+33, 1.64772923719e+33, 2.2114160575e+33, 2.37942340721e+33, 1.83455769713e+33, 2.04200699334e+33, 2.42116213051e+33, 1.95113390103e+33, 2.05317281172e+33, 2.3668519475e+33, 2.07355503262e+33, 1.61643166914e+33, 2.08306944193e+33, 1.84652547594e+33, 2.22696805867e+33, 2.33884296911e+33, 2.33105831045e+33, 2.1501133085e+33, 2.27996712031e+33, 2.27569091886e+33, 2.14242405809e+33, 1.97286525029e+33, 1.77937470081e+33, 2.33282821471e+33, 1.81892363218e+33, 2.3855754721e+33, 2.29943937023e+33, 2.08965708799e+33, 2.03270740927e+33]

sumCO = 0
for numb in CO_Mass_ddt:
	sumCO = sumCO + numb
print(sumCO)

totalnumberCOmass = len(CO_Mass_ddt)
averageCOmass = sumCO/totalnumberCOmass

sumsqauredCOmass = 0
for pt in CO_Mass_ddt:
	oneterm = (pt - averageCOmass)**2
	sumsqauredCOmass = oneterm + sumsqauredCOmass
	

print(sumsqauredCOmass)
totalsqrtCOmass = np.sqrt(1.0/(totalnumberCOmass -1))
sumsqrtCOmass = np.sqrt(sumsqauredCOmass)
SDCOmass = totalsqrtCOmass*sumsqrtCOmass


Hybrid_Mass_ddt =[2.29065506697e+33, 2.37429522308e+33, 1.9619998193e+33, 2.21585165123e+33, 2.36168155367e+33, 2.06264162216e+33, 2.17596605793e+33, 2.44833856567e+33, 1.97386459065e+33, 1.98290439337e+33, 2.38258128395e+33, 2.33195693878e+33, 1.97782335311e+33, 2.20336841115e+33, 2.01128279706e+33, 2.2960275682e+33, 2.43272122416e+33, 2.38432303364e+33, 2.24649942374e+33, 2.30417250882e+33, 2.30262233397e+33, 2.28256434994e+33, 1.88152602291e+33, 2.24919320356e+33, 2.3933694729e+33, 2.16475962152e+33, 2.38200578996e+33, 2.33982006123e+33, 2.37956538463e+33, 2.29544800586e+33]

sumHY = 0 
for numb in Hybrid_Mass_ddt: 
	sumHY = sumHY + numb

totalnumberHYmass = len(Hybrid_Mass_ddt)
averageHYmass = sumHY/totalnumberHYmass

sumsqauredHYmass = 0 
for pt in Hybrid_Mass_ddt: 
	oneterm = (pt - averageHYmass)**2
	sumsqauredHYmass = oneterm + sumsqauredHYmass

print(sumsqauredHYmass)
totalsqrtHYmass = np.sqrt(1.0/(totalnumberHYmass -1))
sumsqrtHYmass = np.sqrt(sumsqauredHYmass)
SDHYmass = totalsqrtHYmass*sumsqrtHYmass


gpermsun = 1.988435e33
b = []
sumb = 0
for fname in filelistHY:
        data = np.loadtxt(fname)
        x = data[-1][13]
        bsolar = x/gpermsun
        b.append(bsolar)
        sumb = sumb + bsolar
totalnumberHY = len(b)       #find the length of the array: total #
averageHYIGE = sumb/totalnumberHY

sumsqauredHY = 0
for pt in b: 
	oneterm = (pt - averageHYIGE)**2
	sumsqauredHY = oneterm + sumsqauredHY

print(sumsqauredHY)
totalsqrtHY = np.sqrt(1.0/(totalnumberHY -1))
sumsqrtHY= np.sqrt(sumsqauredHY)
SDHYIGE = totalsqrtHY*sumsqrtHY
  

#plt.plot(Hybrid_Mass_ddt, b, 'o',label = 'Hybrid', color = 'r')
#fig2, ax2 = plt.subplots()
#ax2.add_patch(patches.Rectangle((averageHYIGE - SDHYIGE , averageHYmass - SDHYmass), 2* SDHYmass, 2* SDHYIGE,  linewidth=1,edgecolor='r',facecolor='red')


#CO model
gpermsun = 1.988435e33 # grams/Msun
a = []
suma = 0
for fname in filelistCO:
	print(fname)
	data = np.loadtxt(fname)
	x = data[-1][13]   #final estimated mass
	xsolar = x/gpermsun        #convert to solar mass
	a.append(xsolar)
	#print(xsolar)
	suma = suma + xsolar
	print(suma)

#a.sort()                       # sort numbers in order
print(a)
totalnumber = len(a)       #find the length of the array: total number

averageCOIGE = suma/totalnumber

sumsqaured = 0 
for pt in a: 
    oneterm = (pt - averageCOIGE)**2
    sumsqaured = oneterm + sumsqaured

print(sumsqaured)
totalsqrt = np.sqrt(1.0/(totalnumber -1))
sumsqrt = np.sqrt(sumsqaured)
SDCOIGE = totalsqrt*sumsqrt


yC = averageCOIGE- SDCOIGE
xC = averageCOmass- SDCOmass
print(xC)
print(yC)
yH = averageHYIGE - SDHYIGE
xH = averageHYmass - SDHYmass
fig,ax1 = plt.subplots()

plt.plot(np.array(CO_Mass_ddt)/gpermsun, a, "o", label ='CO', color = 'b')
plt.plot(np.array(Hybrid_Mass_ddt)/gpermsun, b, "o", label = 'Hybrid', color = 'r')

plt.xlabel(r'Mass with $\rho_7>2$ at DDT (M$_\odot$)')
plt.ylabel('Estimated IGE Yield (M$_\\odot$)')

ax1.add_patch(patches.Rectangle((xC/gpermsun, yC), 2*SDCOmass/gpermsun, 2*SDCOIGE, alpha=0.25,edgecolor='b',facecolor='b'))
ax1.add_patch(patches.Rectangle((xH/gpermsun, yH), 2* SDHYmass/gpermsun, 2* SDHYIGE ,alpha=0.25,edgecolor='r',facecolor='r'))
plt.tight_layout()
plt.savefig('Fig5withSD_fixed_plot.pdf')
#plt.show()
