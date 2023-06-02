import numpy as np
import matplotlib.pyplot as plt

# n - количество точек в диапазоне
n = 64
# секунды дискредтных значений времени
t = np.linspace(0, 1, n, endpoint=True)
# Амплитуды 2,4 вольта
A1 = 2
A2 = 4
# Частота гармонического сигнала 5, 2, (fo1 + fo2) / 2 кГц
fo1 = 5
fo2 = 2
fo = (fo1 + fo2) / 2
# Начальная фаза сигнала
phi = 0
# Скорость заглухания сигнала
a = 3

x = A1*np.sin(np.pi*t*fo1+phi)

Fs_lst = np.array([10, 25, 50, 75])

fig = plt.figure(figsize=(12, 6), dpi=80)

for i in range(4):
    tt = np.linspace(0, 1, int(1/(1/Fs_lst[i])), endpoint=True)
    plt.subplot(2, 2, i+1)
    plt.title('Fs = {}'.format(Fs_lst[i]))
    plt.plot(t, x, '-', linewidth=2.0)
    plt.plot(tt, A1*np.sin(np.pi*tt*fo+phi), '--o', linewidth=1.5, markersize=8)
    plt.step(tt, A1*np.sin(np.pi*tt*fo+phi), linewidth=1.5)
    plt.grid()
    plt.xlim([0, 1])
    plt.tight_layout()
plt.show()