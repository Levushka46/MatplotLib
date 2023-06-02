import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft

N = 100

# Random array of ones and zeros
np.random.seed(6)
mod_rand = np.random.randint(0, 2, 40)

# Repeat number of ones and zeros
mod_fsk = np.repeat(mod_rand, repeats=N)

# FSK signal
M = mod_fsk.size
freq = np.zeros(M)
freq[freq == 0] = 50
freq[freq == 1] = 75


Ac = 2
sig_ask = Ac * np.cos(freq * 2.0 * np.pi * np.linspace(0, 1, M))

# PLot results
plt.figure(figsize=(16, 6), dpi=80)
plt.subplot(2, 1, 1)
plt.title('Digital signal')
plt.plot(mod_fsk, color='C0', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)

plt.subplot(2, 1, 2)
plt.title('FSK-signal')
plt.plot(mod_fsk, '--', color='C0', linewidth=2.0)
plt.plot(sig_ask, '-', color='C1', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)
plt.show()