import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
T = 1  # Период сигнала
E = 1  # Амплитуда
t1 = 0.125 * T  # Начало сигнала
t2 = 0.2 * T  # Конец сигнала

# Основная частота
omega1 = 2 * np.pi / T

# Число гармоник
N = 10

# Коэффициенты Фурье
def a_n(n):
    if n == 0:
        return (2 / T) * 0.5 * E * (t2 - t1)
    else:
        return (2 / T) * 0.5 * E * (np.sin(n * omega1 * t2) - np.sin(n * omega1 * t1)) / (n * omega1)

def b_n(n):
    return 0  # Для чётного сигнала синусоидальная составляющая равна 0

# Амплитуда и фаза
def A_n(n):
    return np.sqrt(a_n(n)**2 + b_n(n)**2)

def phi_n(n):
    return 0 if n == 0 else np.arctan2(b_n(n), a_n(n))

# Вычисления
n_values = np.arange(1, N + 1)
amplitudes = [A_n(n) for n in n_values]
phases = [phi_n(n) for n in n_values]

# Построение графиков
plt.figure(figsize=(12, 6))

# Амплитудный спектр
plt.subplot(1, 2, 1)
plt.stem(n_values, amplitudes, basefmt=" ")
plt.title("Амплитудный спектр")
plt.xlabel("Гармоника n")
plt.ylabel("Амплитуда A_n")
plt.grid()

# Фазовый спектр
plt.subplot(1, 2, 2)
plt.stem(n_values, phases, basefmt=" ")
plt.title("Фазовый спектр")
plt.xlabel("Гармоника n")
plt.ylabel("Фаза φ_n (рад)")
plt.grid()

plt.tight_layout()
plt.show()

