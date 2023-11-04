# OFDM experiments and simulation

import matplotlib.pyplot as plt
import numpy as np
# import scipy as sc

if __name__ == "__main__":
    t = np.arange(0.0, 1.0, 0.001)
    f = 10
    sine = np.sin(2*np.pi*f*t)

    fig, ax = plt.subplots()
    ax.plot(t,sine)
    ax.grid()

    plt.show()
