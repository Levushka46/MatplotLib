import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft

# функция АМ-сигнала
def signal_am(amp=1.0, km=0.25, fc=10.0, fs=2.0, period=100):
    """
    Параметры
    ----------
    amp : float
        амплитуда несущего колебания
    km : float
         коэффициент модуляции 0 <= km < 1
    fc : float
        частота несущего сигнала
    fs : float
        частота модулирующего (информационного) сигнала
    period : integer
        Количество точек для сигнала (такое же, как период)
    """
    tt = 2.0 * np.pi * np.linspace(0, 1, period)
    return amp * (1 + km * np.cos(fs * tt)) * np.cos(fc * tt)


N = 1024

# Генерирование AM-сигнала

fc = 40  # Частоты несущего сигнала
fs = 8# Частота модуляции
km = [0.35, 0.85, 5] #коэффициент модуляции

sig = [signal_am(amp=2.75, km=i, fc=fc, fs=fs, period=N) for i in km]

# Вычисление спектра мощности
sft = np.abs(fft(sig, axis=1)) / N / 0.5

plt.figure(figsize=(16, 8))
for i, freq in enumerate(km):
    plt.subplot(len(km), 2, 2 * i + 1)
    if i == 0:
        plt.title('AM-сигнал')
    plt.plot(sig[i])
    plt.xlim([0, N - 1])
    plt.grid(True)

    plt.subplot(len(km), 2, 2 * i + 2)
    if i == 0:
        plt.title('Спектр')
    plt.plot(sft[i])
    plt.xlim([0, N // 2 - 1])
    plt.grid(True)
plt.show()