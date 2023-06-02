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

# ---------------------------------------------------------------
# Графики
# x = A1 * np.sin(np.pi*t*fo1+phi)
# x = A1 * np.sin(np.pi*t*fo1+phi) + A2 * np.cos(np.pi*t*fo2+phi)
x = np.exp(-a*t) * A1 *np.sin(np.pi*t*fo1 + phi)

def plt_sel(s, *args, **kwargs):
    if s == 0:
        return plt.plot(*args)
    if s == 1:
        return plt.stem(*args, **kwargs)
    if s == 2:
        return plt.step(*args)

# Заголовки графиков
t_titles = ['Аналоговый', 'Дискретный', 'Квантованный']

fig = plt.figure(figsize=(16, 4), dpi=80)
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.title(t_titles[i])
    plt_sel(i, t, x, use_line_collection=True)
    plt.xlim([0, 1])
    plt.yticks(np.linspace(np.floor(np.min(x)), np.ceil(np.max(x)), 9))
    plt.grid(True)

    # change plot view
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))

plt.show()