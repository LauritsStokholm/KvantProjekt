import numpy as np
import matplotlib.pyplot as plt
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
          'figure.figsize'      : [8.5, 6.375],
          'legend.frameon'      : False
          }

plt.rcParams.update(params)
plt.rc('text',usetex =True)
plt.rc('font', **{'family' : "sans-serif"})
# %% def constants
n = 1
a0 = 1
l=1
# %% def functions
def asump(r):
    return (r/a0)**(n-1) * np.exp(-r/(n*a0))

def func11(r):
    led = n+np.sqrt(l*(l+1))
    del1 = np.power((r/a0),led)
    del2 = np.exp((1-(r/a0))/(n+np.sqrt(l*(l+1))))
    result = ((del1*del2)/r)
    return result

# %% run functions in r interval
interval = np.pi

r = np.linspace(0,30,100000)
AssumpR = asump(r)
function11 = func11(r)

fig1,ax1 = plt.subplots()
ax1.plot(r,func11(r),'r', color='black', linestyle='--',label='WKB')
ax1.plot(r,asump(r),'b',color='grey', label='Eksakt')
ax1.legend()
plt.xlabel(r'$r$')
plt.ylabel(r'$R(r)$')
plt.ylim([-0.1,2.5])
fig1.savefig("sammenligning.png")
plt.show()
