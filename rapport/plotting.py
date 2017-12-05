#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sp
import scipy.special as misc
import numpy.polynomial.hermite as hermite
import sys
print(sys.version)
# %% smukplot
# MatploLib koerer TeX
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
hbar = 1
m = 1
omega = 1
# %% def function
# psi n
def psi(x,n):
    dimVar = np.sqrt((m*omega)/hbar)*x

    hermArray = np.zeros(n+1)
    hermArray[n] = 1

    H_n = hermite.hermval(dimVar,hermArray)

    Del1 = (m*omega/(np.pi*hbar))**(1/4)
    Del2 = 1/(np.sqrt(2**n)*misc.factorial(n))
    Del3 = H_n*np.exp(-dimVar**2/2)

    psi = Del1 * Del2 * Del3
    return psi

#potential
def pot(x):
    v = 1/2 * m * omega**2 * x**2
    return(v)

# %% udregn v og psi og x
x = np.linspace(-np.pi,np.pi,1000)
v = pot(x)
psi = psi(x,0)
# %% plot
fig,ax = plt.subplots()
ax.plot(x,v, color="red",linestyle='-',label="lol")
ax.plot(x,psi**2, color='#000000',label="cake")
ax.legend()
plt.show()
