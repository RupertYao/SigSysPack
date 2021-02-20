from math import pi, sin

import matplotlib.pyplot as plt
import numpy as np

import SigSysPack.Convolution as Conv
import SigSysPack.FourierTransform as FT
from SigSysPack import FFT

# test Convolution.py


def func1(t):
    if abs(t) <= 0.5:
        return 1
    else:
        return 0


def func2(t):
    if abs(t) <= 1:
        return 1
    else:
        return 0


a = [1, 2, 3]
b = [1, 2, 3, 4]
# a = np.random.randn(5)
# print(a)
c = Conv.convolution(a, b)
print(c)
t_res, res = Conv.convolutionIntegral(func1=func1, func2=func2)

plt.plot(t_res, res)
plt.show()

# test FourierTransform.py


def Sa(t):
    # if t >= -1 and t <= 1:
    #     return 1
    # else:
    #     return 0
    if t == 0:
        t = 1e-15
    return sin(t) / t


def Gate(t):
    if abs(t) < 1:
        return pi
    else:
        return 0


omega = np.linspace(-10 * pi, 10 * pi, num=1000)
# omega = np.linspace(-2, 2, num=1000)
res = FT.stft(func=Sa, t=(-100, 100), N=1000, omega=omega)
res = FT.istft(func_freq=Sa, omega=(- 10 * pi, 10 * pi), t=omega)

freq_f = res
print(freq_f[0])
plt.plot(omega, abs(freq_f))
plt.show()

N = 20
n = np.linspace(-N, N, num=2 * N + 1)
f = np.zeros_like(n)
for i in range(len(n)):
    f[i] = Sa(n[i])
omega = np.linspace(-10, 10, num=1000)
res_dtft = FT.dtft(res, N, omega=omega)
res_idtft = FT.idtft(Gate, omega=(-50, 50), K=1000, N=20)

f2 = [1 if i <= 2 and i >= -2 else 0 for i in range(0, 11)]
res_dft = FT.dft(f2)

plt.figure()

plt.subplot(3, 1, 1)
plt.stem(n, f)
plt.stem(n, np.real(res_idtft))
plt.subplot(3, 1, 2)
plt.plot(omega, abs(res_dtft))
plt.subplot(3, 1, 3)
plt.stem([i for i in range(0, 11)], abs(res_dft))
plt.ylim([-0.1, 5.1])
plt.grid(True)
plt.show()

# test FFT.py


def Sa(t):
    if t == 0:
        t = 1e-9
    return sin(t) / t


def Gate(tao, t):
    if t < -tao / 2 or t > tao / 2:
        return 0
    return 1


t = np.linspace(0, 20, num=20 + 1)
# f = np.sinc(t)

f = np.zeros_like(t)
for i in range(0, len(t)):
    f[i] = Sa(t[i])
    # f[i] = Gate(6, t[i])

F = FFT.fft(f)

plt.figure()

plt.stem(np.abs(F))
plt.show()
