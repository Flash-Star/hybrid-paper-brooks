import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# from Rich Townsend for mesa3
params = {'backend': 'pdf',
          'figure.figsize': [3.38, 3.38],
          'font.family':'serif',
          'font.size':10,
          'font.serif': 'Times Roman',
          'axes.titlesize': 'medium',
          'axes.labelsize': 'medium',
          'legend.fontsize': 8,
          'legend.frameon' : False,
          'text.usetex': True,
          'figure.dpi': 600,
          'lines.markersize': 4,
          'lines.linewidth': 1,
          'lines.antialiased': False,
          'path.simplify': False,
	  # mine below here
	  'legend.numpoints': 1}

matplotlib.rcParams.update(params)

ORANGE     = (0.90,0.60,0.00)
SKY_BLUE   = (0.35,0.70,0.90)
BLUE_GREEN = (0.00,0.60,0.50)
YELLOW     = (0.95,0.90,0.25)
BLUE       = (0.00,0.45,0.70)
VERMILLION = (0.80,0.40,0.00)
RED_PURPLE = (0.80,0.60,0.70)



gpermsun = 1.988435e33 # grams/Msun

#import data
data = np.genfromtxt("yields_ige_ni56_KE.dat", names=True)

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


b = data['CONe_IGE']
sumb = sum(b)
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
a = data['CO_IGE']
suma = sum(a)
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

plt.plot(np.array(CO_Mass_ddt)/gpermsun, a, 'rs', label ='CO')
plt.plot(np.array(Hybrid_Mass_ddt)/gpermsun, b, 'bo', label = 'CONe')

plt.xlabel(r'Mass with $\rho_7>2$ at DDT (M$_\odot$)')
plt.ylabel(r'IGE Yield (M$_\odot$)')

ax1.add_patch(patches.Rectangle((xC/gpermsun, yC), 2*SDCOmass/gpermsun, 2*SDCOIGE, alpha=0.25,edgecolor='r',facecolor='r'))
ax1.add_patch(patches.Rectangle((xH/gpermsun, yH), 2* SDHYmass/gpermsun, 2* SDHYIGE ,alpha=0.25,edgecolor='b',facecolor='b'))

w16_cone_x = 0.5*(1.057+0.848)
w16_cone_dx = 0.5*(1.057-0.848)
w16_cone_y = 0.5*(1.087+0.865)
w16_cone_dy = 0.5*(1.087-0.865)

w16_co_x = 0.5*(1.062+0.858)
w16_co_dx = 0.5*(1.062-0.858)
w16_co_y = 0.5*(1.185+1.05)
w16_co_dy = 0.5*(1.185-1.05)

ax1.add_patch(patches.Rectangle((w16_co_x-w16_co_dx,w16_co_y-w16_co_dy), 2*w16_co_dx, 2*w16_co_dy, alpha=0.1, edgecolor='r',facecolor='r', linestyle='--'))
ax1.add_patch(patches.Rectangle((w16_cone_x-w16_cone_dx,w16_cone_y-w16_cone_dy), 2*w16_cone_dx, 2*w16_cone_dy, alpha=0.1, edgecolor='b',facecolor='b', linestyle='--'))

plt.legend(loc='lower right')

plt.xlim([0.8,1.3])
ax1.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ax1.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

plt.tight_layout()
plt.savefig('ige_v_mass_at_high_dens.pdf')
#plt.show()
