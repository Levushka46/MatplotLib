import numpy as np
import array as arr
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, butter, firls, remez, firwin, firwin2, group_delay
from scipy.fftpack import fft, fftshift

# 5_1_1
N = 512
f = np.linspace(0, 1, N, endpoint=True)
print("Списки однородных коэффициентов")
b1 = [1, 1, 1]
plt.figure(figsize=(16, 4))
plt.subplot(1, 2, 1)
for i in range(3):
    print(b1)
    _, h = freqz(b1, N)
    h = np.abs(h)
    plt.plot(f, h/np.max(h))
    plt.xlim([0, 1])
    plt.grid(True)
    b1.append(1)
plt.xlabel('Нормализованная частота')
plt.title('Частотная характеристика фильтра с однородными коэффициентами')
print("")

print("Списки неоднородных коэффициентов")

# 5_1_2
b2 = [0.5, 1, 0.5]
plt.subplot(1, 2, 2)
print(b2)
_, h = freqz(b2, N)
h = np.abs(h)
plt.plot(f, h / np.max(h))
plt.xlim([0, 1])
plt.grid(True)

b2 = [0.25, 0.5, 0.5, 0.25]
plt.subplot(1, 2, 2)
print(b2)
_, h = freqz(b2, N)
h = np.abs(h)
plt.plot(f, h / np.max(h))
plt.xlim([0, 1])
plt.grid(True)

b2 = [0.15, 0.20, 0.30, 0.20, 0.15]
plt.subplot(1, 2, 2)
print(b2)
_, h = freqz(b2, N)
h = np.abs(h)
plt.plot(f, h / np.max(h))
plt.xlim([0, 1])
plt.grid(True)

plt.xlabel('Нормализованная частота')
plt.title('Частотная характеристика фильтра с неоднородными коэффициентами')
plt.show()