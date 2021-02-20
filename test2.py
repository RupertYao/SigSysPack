from math import pi
import numpy as np
import matplotlib.pyplot as plt

import SigSysPack.FourierTransform as FT
from SigSysPack import FFT


def Gate(tao, t):
    if np.abs(t) <= np.abs(tao) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = np.linspace(-10, 10, num=21)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    F = FT.dft(f)
    # F = FT.idft(f)

    plt.subplot(2, 1, 1)
    plt.stem(t, f)
    plt.subplot(2, 1, 2)
    plt.stem(np.abs(F))
    plt.show()

    N = 1000
    t_length = 20
    T = t_length / N
    t = np.linspace(0, N - 1, num=N) * T - t_length / 2
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(2, t[i])

    w_length = 2 * pi / T
    W = w_length / N
    F = T * FFT.fft(f)
    F = FFT.fft_shift(F)
    w = np.linspace(0, N - 1, num=N) * W - w_length / 2

    plt.subplot(2, 1, 1)
    plt.plot(t, f)
    plt.subplot(2, 1, 2)
    plt.plot(w, np.abs(F))
    # plt.xlim([-3 * pi, 3 * pi])
    plt.xlim([-10 * pi, 10 * pi])
    plt.grid()
    plt.show()
