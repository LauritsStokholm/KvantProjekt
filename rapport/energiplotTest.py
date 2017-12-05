import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sp

# %% Def constants
hbar = sp.hbar
e = -1.60217e-19
m = sp.electron_mass
eps0 = sp.epsilon_0
Ry = 13.6 * 8.854187817620389e-12
# %% Def funcs
def actualEnergi(n):
    energi = -(m/(2*(hbar)**2) * ((e**2)/(4*np.pi*eps0))**2)*(1/n**2)
    return energi

def wkbEnergi(n):
    l = 1
    energi = -Ry/(n+np.sqrt(l*(l+1)))**2
    return energi

# %% values
n = np.arange(1,10)
EActual = actualEnergi(n)
EWkb = wkbEnergi(n)

# %% plot de plot
fig,ax = plt.subplots()
ax.plot(n,EActual,'k.', label = "Exact Energies")
ax.plot(n,EWkb,'b.', label = "WKB approximation Energies")
ax.legend()
plt.show()
