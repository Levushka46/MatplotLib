import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

# 3
N=128 # Частота дискретизации
t=np.linspace(0, 1, N)# Отсчёты времени
F=[5,10] # Частоты сигналов
A=[8,15,20] # Амплитуды сигналов
phi=[2*np.pi/2, np.pi/3] # Фазы сигналов

alpha=3 # Параметр затухания сигнала

# Шумы
noise1 = np.random.randn(N)*1.2
noise2 = np.random.randn(N)*2
noise3 = np.random.randn(N)*1.75
noise4 = np.random.randn(N)*1.1

# Функции сигналов
X = [ A[0]*np.sin(2*np.pi*t*F[0]), #x1
      A[1]*np.sin(2*np.pi*t*F[0]), #x2
      A[2]*np.sin(2*np.pi*t*F[0] + phi[0]), #x3
      A[0]*np.cos(2*np.pi*t*F[1] + phi[1]) ] #x4

# Добавление шума к сигналу
X_noise = [X[0]+noise1, X[1]+noise2, X[2]+noise3, X[3]+noise4]# Зашумленные сигналы

# Параметр сглаживающего фильтра (длина последовательности)
windowSize = 3
h = (1/windowSize)*np.ones(windowSize)

#Свертка зашумленного сигнала с фильтром
X_filt = [np.convolve(X_noise[0],h,'same'), np.convolve(X_noise[1],h,'same'), np.convolve(X_noise[2],h,'same'), np.convolve(X_noise[3],h,'same')]

# Визуализация сигналов
for i in range(0, 4):
    fig = plt.figure(figsize=(16, 5), dpi=100)
    plt.subplot(2, 2, 1)
    plt.title('Сигнал+шум')
    plt.plot(X_noise[i])
    plt.xlim([0, N - 1])
    plt.xlabel('samples')
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.title('Сигнал сглаженный')
    plt.plot(X_filt[i])
    plt.xlim([0, N - 1])
    plt.xlabel('samples')
    plt.grid()
    plt.show()