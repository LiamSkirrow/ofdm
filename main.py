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

    f1 = 312500
    sine0  = 0.5*np.sin(2*np.pi*f1*t)
    f2 = 625000
    sine0 += 2*np.sin(2*np.pi*f2*t)
    f3 = 937500
    sine0 += 3*np.sin(2*np.pi*f3*t)
    
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
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    ax1.plot(freqBins, mapped_ifft.real, label='real')
    ax1.plot(freqBins, mapped_ifft.imag, '--', label='imaginary')

    calc_fft = fft(mapped_ifft)
    ax2.plot(t, calc_fft)

    ax3.plot(t, sine0)
    ax4.plot(freqBins, np.abs(fft(sine0)), label='real')
    # ax4.plot(freqBins, fft(sine0).imag, '--', label='imaginary')

    ax1.grid()
    ax1.legend()
    ax2.grid()
    ax2.legend()
    ax3.grid()
    ax3.legend()

    print(freqBins)

    plt.show()
