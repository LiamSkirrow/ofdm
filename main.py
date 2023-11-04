# OFDM experiments and simulation

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft

""" plan
1- create a placeholder list of complex numbers and perform the IFFT on them
2- mix the Re and Im outputs of the IFFT with in-phase and quadrature carrier frequency, repsectively
3- add signals together to produce final carrier signal
"""

if __name__ == "__main__":
    t = np.arange(0.0, 0.000003200, 0.000000050) # 0 -> 3.2us, incr 50ns
    
    N = 64
    n = np.arange(N)
    fs = 1/0.000000050  # 20Msps -> 50ns sampling period
    T = N/(fs)          # 64 * 1/20MHz -> 64 * 50ns -> 3.2us
    freqBins = n/T      # 64 bins of 312.5kHz spacing (20MHz/64)
    
    mapped_complex_values = np.array([1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,
                                      1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j, 1+1j,])

    mapped_ifft = ifft(mapped_complex_values)

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    ax1.plot(freqBins, mapped_ifft.real, label='real')
    ax1.plot(freqBins, mapped_ifft.imag, '--', label='imaginary')

    calc_fft = fft(mapped_ifft)
    ax2.plot(t, calc_fft)

    ax1.grid()
    ax1.legend()
    ax2.grid()
    ax2.legend()

    print(freqBins)

    plt.show()
