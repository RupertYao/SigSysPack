import numpy as np
import matplotlib.pyplot as plt

from SigSysPack import FFT


def Signal(t):
    if t <= 10 or t >= 118:
        return 1
    return 0


if __name__ == "__main__":
    N = 128
    t = np.linspace(0, N - 1, num=N)
    f = np.zeros_like(t)
    for i in range(len(t)):
        f[i] = Signal(t[i])

    plt.subplot(2, 1, 1)
    plt.plot(t, f)

    F = FFT.fft(f) / np.sqrt(128)
    F = FFT.fft_shift(F)
    plt.subplot(2, 1, 2)
    plt.plot(t, np.abs(F))

    plt.show()
