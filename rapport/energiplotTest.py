import numpy as np
import matplotlib as mpl
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
          'figure.figsize'      : [10, 7],
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


l_width = 1.7
n_width = 1.9


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



noOfl = 3
n_start = 2
n_end = 8
l_start = 4

fig2,ax2 = plt.subplots()
for n in range(n_start,n_end):
    #WKB delen
    for l in range(0,noOfl):
        linjePlot(linjer(l_width,l_start-1+l),wkbEnergi(n,l),ax2,'k')
    linjePlot(linjer(n_width,1),actualEnergi(n),ax2,'k')



ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

ticks = [r"$\text{Eksakt}$",r"$\text{WKB}$"]
for l in range(0,noOfl):
    ticks.append(r"$l = %s $ "%(l))


xTick = [2.3, 3.5]
for i in range(0,noOfl):
    xTick.append(i + l_start+(l_width-1)/2)


plt.xticks(xTick, ticks)

# plt.tight_layout()
plt.ylabel(r"$E \ [\si{\electronvolt}]$")
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on')

fig2.savefig("energyPlot.png")
plt.tight_layout()
# plt.grid()


plt.show()
