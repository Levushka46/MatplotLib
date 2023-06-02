# Дискретизация сигнала 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift

# Частота дискретизации
N = 256

# Вектор временных отсчетов
t = np.linspace(0, 1, N)

# Частоты, амплитуды составляющих сигналов
f = [5, 10, 15]
A = [15, 8, 20]

# Коэффициент затухания сигнала
alpha = 3

# Сигналы
x1 = A[0] * np.cos(np.pi*f[0]*t)
x2 = x1 + A[1]*np.cos(np.pi*f[1]*t)
x3 = x1 + x2 + np.exp(-alpha*t)*A[2]*np.cos(np.pi*f[2]*t)

y=[0, 0, 0]
fig = plt.figure(figsize=(30, 17), dpi=85)
#Выбор моделируемой компоненты и запись отсчётов
for i in range (1, 4):
    if (i==1):
        y[i-1] = x1
    elif (i==2):
        y[i-1] = A[i-1]*np.cos(np.pi*f[1]*t)
    elif (i==3):
        y[i-1] = np.exp(-alpha*t)*A[i-1]*np.cos(np.pi*f[2]*t)

# Визуализация компонент сигнала во временном пространстве
# Сигнал во временной области
    plt.subplot(4, 3, i)
    plt.title('Signal Component ' + str(i))
    plt.plot(y[i-1])
    plt.xlim([0, N-1])
    plt.xlabel('samples')
    plt.grid()

# Получение результирующего сигнала
y_sum = y[0]+sum(y)#сумма всех компонент исходного сигнала
plt.subplot(4, 3, 4)
plt.title('Result Signal')
plt.plot(y_sum)
plt.xlim([0, N-1])


# Вычисление ДПФ. Х - комплексные коэффициенты ДПФ, содержащие аплитуды гармонических составляющих сигнала x
X = fft(y_sum)
# Вывод коэффициентов ДПФ
print(X)

# Вычисление модуля ДПФ
X_mag = 2*np.abs(X) / N

# Вычисление фазы
Phase = np.angle(X)

# Вещественные и мнимые составляющие
plt.subplot(4, 3, 5)
plt.title('Real/Imag')
plt.plot(np.real(X))
plt.plot(np.imag(X))
plt.xlim([0, N//2-1])
plt.xlabel('frequency')
plt.grid()
plt.tight_layout()

# Спектр мощности сигнала
plt.subplot(4, 3, 6)
plt.title('Spectrum')
plt.stem(X_mag, use_line_collection=True, basefmt='C0')
plt.xlim([0, N//2-1])
plt.xlabel('frequency')
plt.grid()
plt.tight_layout()

#Выбор коэффициентов и обратное ДПФ
X[0:2]=0
X[3: ]=0
x_result=ifft(X)# Обратное ДПФ
plt.subplot(4, 3, 7)
plt.title('Update signal component')
plt.plot(N*t, x_result)
plt.show()
