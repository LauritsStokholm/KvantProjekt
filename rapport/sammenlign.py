import numpy as np
import matplotlib.pyplot as plt

# %% def constants
n = 1
a0 = 1
l=1
# %% def functions
def asump(r):
    return (r/a0)**(n-1) * np.exp(-r/(n*a0))

def func11(r):
    led = n+np.sqrt(l*(l+1))
    del1 = np.float_power((r/a0),(2.1))
    del2 = np.exp((1-(r/a0))/(n+np.sqrt(l*(l+1))))
    result = ((del1*del2)/r)
    return result

# %% run functions in r interval
interval = np.pi

r = np.linspace(-interval,interval,1)
AssumpR = asump(r)
function11 = func11(r)
