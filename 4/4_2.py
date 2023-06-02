import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft

# функция ЧМ-сигнала
def signal_fm(amp=1.0, kd=0.25, fc=10.0, fs=2.0, period=100):
    """
    Параметры
    ----------
    amp : float
        амплитуда несущего колебания
    kd : float
         девиация частоты, kd < period/4
    fc : float
        частота несущего сигнала
    fs : float
        частота модулирующего (информационного) сигнала
    period : integer
        Количество точек для сигнала (такое же, как период)
    """
    tt = 2.0 * np.pi * np.linspace(0, 1, period)
    return amp * np.cos(fc * tt + kd/fs * np.sin(fs * tt))

# Cигналы с частотной модуляцией в зависимости от значения девиации частоты:
N = 1024

fs = [7, 14, 25]  # Частота модуляции
fс = 60  # Частоты несущего сигнала
kd = 25  # Коэффициент частотной модуляции

sig = [signal_fm(amp=2.0, kd=kd, fc=fс, fs=i, period=N) for i in fs]

# Calculate FFT
sft = np.abs(fft(sig, axis=1)) / N / 0.5

plt.figure(figsize=(16, 8))
for i, freq in enumerate(fs):
    plt.subplot(len(fs), 2, 2 * i + 1)
    if i == 0:
        plt.title('FM-signal')
    plt.plot(sig[i])
    plt.xlim([0, N // 2 - 1])
    plt.grid(True)

    plt.subplot(len(fs), 2, 2 * i + 2)
    if i == 0:
        plt.title('Spectrum')
    plt.plot(sft[i])
    plt.xlim([0, N // 2 - 1])
    plt.grid(True)
plt.show()