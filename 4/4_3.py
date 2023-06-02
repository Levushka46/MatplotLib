import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft

N = 64

# Random array of ones and zeros
np.random.seed(6)
mod_rnd = np.random.randint(0, 2, 40)

# Repeat number of ones and zeros
mod_ask = np.repeat(mod_rnd, repeats=N)

# ASK signal
M = mod_ask.size
fc = 60
sig_ask = mod_ask * np.sin(fc * 2.0 * np.pi * np.linspace(0, 1, M))

# PLot results
plt.figure(figsize=(16, 6), dpi=80)
plt.subplot(2, 1, 1)
plt.title('Digital signal')
plt.plot(mod_ask, color='C0', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)

plt.subplot(2, 1, 2)
plt.title('ASK-signal')
plt.plot(mod_ask, '--', color='C0', linewidth=2.0)
plt.plot(sig_ask, '-', color='C1', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)
plt.show()