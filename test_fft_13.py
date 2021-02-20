import numpy as np
import matplotlib.pyplot as plt

from SigSysPack import FFT
import SigSysPack.FourierTransform as FT


def Gate(tao, t):
    if np.abs(t) <= np.abs(tao) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = np.linspace(0, 13**2 - 1, num=13**2)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    F = FT.dft(f)
    # F = FFT.fft(f)
    F2 = FFT.fft_radix_13(f)

    plt.subplot(3, 1, 1)
    plt.stem(t, f)
    plt.subplot(3, 1, 2)
    plt.stem(np.abs(F2))
    plt.subplot(3, 1, 3)
    plt.stem(np.abs(F) - np.abs(F2))
    plt.show()
