# OFDM experiments and simulation

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
# import scipy as sc

if __name__ == "__main__":
    t = np.arange(0.0, 1.0, 0.001)
    f = 10
    sine = np.sin(2*np.pi*f*t)

    Xsine = fft(sine)
    N = len(Xsine)
    n = np.arange(N)
    T = N/(1/0.001)
    freq = n/T

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    ax1.plot(t,sine)
    ax2.plot(freq,np.abs(Xsine))

    ax1.grid()
    ax2.grid()

    plt.show()
