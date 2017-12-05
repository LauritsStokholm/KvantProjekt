import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sp
import scipy.special as misc
import numpy.polynomial.hermite as hermite
# %% smukplot
# MatploLib koerer TeX

# %% def constants
hbar = 1
m = 1
omega = 1
x0 = 2
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

# wkb psi
def wkbPsi(x,n):

    E =  (m*omega**2 * x0**2)/2
    x0 = (2*E)/m*omega**2
    p = np.sqrt(2*m(E-(m*hbar*omega**2 * x**2)/2))
    del1 = C/np.sqrt(p)
    del2 = np.cos(((n*np.pi)/(2))*((E)/(hbar*omega))*(np.arcsin((x/x0))+((x)/(x0))*np.sqrt(1-(x**2/x0**2))))
    return del1*del2

# %% udregn v og psi og x1
x = np.linspace(-x0,x0,1000)
v = pot(x)
psi1 = psi(x,0)
psiWkb1 = (x,0)
# %% plot
fig,ax = plt.subplots()
ax.plot(x,v, color="red",linestyle='-',label="V(x)")
ax.plot(x,psi1**2*10, color='#000000',label="|psi|^2 n = 0")
ax.plot(x,psiWkb1[0], color='green')
ax.legend()
plt.show()
