import SigSysPack.FourierTransform as FT

import numpy as np
import matplotlib.pyplot as plt
from math import pi


def f(n):
    if abs(n) <= 2:
        return 1
    return 0


if __name__ == "__main__":
    N = 10
    k = np.linspace(-N, N, num=2 * N + 1)
    x = np.zeros_like(k)
    for n in range(0, len(k)):
        x[n] = f(k[n])

    w = np.linspace(-3 * pi, 3 * pi, num=1185)
    X = FT.dtft(x, N, omega=w)

    plt.subplot(2, 1, 1)
    plt.stem(k, x)
    plt.subplot(2, 1, 2)
    plt.plot(w, np.abs(X))

    plt.show()
