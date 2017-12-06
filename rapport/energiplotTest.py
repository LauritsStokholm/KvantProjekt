import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sp
import sys
print(sys.version)
params = {'legend.fontsize'     : '20',
          'axes.labelsize'      : '20',
          'axes.titlesize'      : '20',
          'xtick.labelsize'     : '20',
          'ytick.labelsize'     : '20',
          'legend.numpoints'    : 1,
          'text.latex.preamble' : [r'\usepackage{siunitx}',
                                   r'\usepackage{amsmath}'],
          'axes.spines.right'   : False,
          'axes.spines.top'     : False,
          'figure.figsize'      : [10, 8],
          'legend.frameon'      : False
          }

plt.rcParams.update(params)
plt.rc('text',usetex =True)
plt.rc('font', **{'family' : "sans-serif"})
# %% Def constants
hbar = sp.hbar
e = -1.60217e-19
m = sp.electron_mass
eps0 = sp.epsilon_0
Ry = 13.6#eV      * 8.854187817620389e-12
# %% Def funcs
def actualEnergi(n):
    energi = -Ry/n**2#  (m/(2*(hbar)**2) * ((e**2)/(4*np.pi*eps0))**2)*(1/n**2)
    return energi

def wkbEnergi(n,l):
    under = n+np.sqrt(l*(l+1))
    energi = -Ry/under**2
    return energi

def linjer(width,space):
    x = np.linspace(1+space,width+space)
    return x
def linjePlot(x,Energy,ax,color='k'):
    e_length = np.linspace(1,1,len(x))
    E = Energy*e_length
    ax.plot(x,E,color)


l_width = 1.1
n_width = 1.4


# %% values
n = np.arange(1,10)
EActual = actualEnergi(n)
EWkb = wkbEnergi(n,1)

# %% plot de plot
fig1,ax1 = plt.subplots()
ax1.plot(n,EActual,'r.', label = "Exact Energies")
ax1.plot(n,EWkb,'b.', label = "WKB approximation Energies")
plt.xlabel("n")
plt.ylabel("E [eV]")
ax1.legend(loc=5)




fig2,ax2 = plt.subplots()
for n in range(1,5):
    #WKB delen
    for l in range(1,5):
        linjePlot(linjer(l_width,1+l),wkbEnergi(n,l),ax2,'k')
    linjePlot(linjer(n_width,1),actualEnergi(n),ax2,'k')


plt.show()
