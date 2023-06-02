import numpy as np
import array as arr
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, butter, firls, remez, firwin, firwin2, group_delay
from scipy.fftpack import fft, fftshift

# Задача 5.3
N = 1024
# Генерирование сигнала
t = np.linspace(0, 1, N, endpoint=True)
x = 3*np.cos(2*np.pi*15*t) + 110*np.sin(2*np.pi*106*t) + 100*np.sin(2*np.pi*170*t) + 280*np.sin(2*np.pi*205*t)

# Добавление шума к сигналу
np.random.seed(1)
xn = x + 5*np.random.randn(N)

# Фильтр Кайзера
taps = 160
h = firwin(taps, 0.05, window=('kaiser', 9))
y = lfilter(h, 1, xn)

# Входной сигнал, импульсная характеристика фильтра и выходной сигнал
lst_sig = [xn, h, y]

sig_titles = ['Сигнал+шум', 'Импульсная характеристика фильтра', 'Выделенный сигнал']
fft_titles = ['Спектр сигнала', 'АЧХ фильтра', 'Спектр выделенного сигнала']

plt.figure(figsize=(16, 10))
for i in range(3):
    # Calculate FFTs
    clc_fft = np.abs(fft(lst_sig[i], N))
    clc_fft = 20 * np.log10(10e-11 + clc_fft / np.max(clc_fft))

    # Plot signals
    plt.subplot(3, 2, 2 * i + 1)
    plt.plot(lst_sig[i], color='C' + str(i))
    plt.title(sig_titles[i])
    if (i == 2):
        plt.ylim([-5, 5])
        plt.xlim([taps, lst_sig[i].size // 2 - 1])
    else:
        plt.xlim([0, lst_sig[i].size - 1])
    plt.grid(True)

    plt.subplot(3, 2, 2 * (i + 1))
    plt.plot(clc_fft, color='C' + str(i))
    plt.title(fft_titles[i])
    plt.xlim([0, N // 2 - 1])
    plt.grid(True)
plt.show()