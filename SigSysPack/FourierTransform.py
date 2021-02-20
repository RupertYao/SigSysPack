from math import pi, log2, log
from SigSysPack import FFT
from .pack import FT_pack

import numpy as np


def stft(func, t=(-10, 10), N=1000,
         omega=np.linspace(-3 * pi, 3 * pi, num=1000)):
    """
    连续时间信号的傅里叶变换

    ## Parameters:
    func: function\n
    连续信号在时域关于t的函数

    t: tuple (t1, t2)\n
    在t1到t2的时域区间上，对信号采样

    N: int\n
    时域上的采样数

    omega: class 'numpy.array'\n
    计算omega对应区间上信号的频谱

    ## Return
    result: class 'numpy.ndarray'\n
    result.shape == (len(omega), 1), 为频谱在所规定区间上的值
    """
    t1, t2 = t
    func_t = np.linspace(t1, t2, num=N)
    f = np.zeros_like(func_t)
    for i in range(0, len(func_t)):
        f[i] = func(func_t[i])

    # delta_t = (t2 - t1) / (N - 1)

    # f_freq = delta_t * np.asmatrix(f) * np.exp(
    #     -1j * np.asmatrix(func_t).T * np.asmatrix(omega))
    # # print(omega.shape)
    # result = np.asarray(f_freq).reshape((len(omega),))
    result = FT_pack.stft(f, func_t, t, N, omega)
    return result


def istft(func_freq, omega=(-5 * pi, 5 * pi), K=1000,
          t=np.linspace(-10, 10, num=1000)):
    """
    连续时间信号频谱的傅里叶逆变换

    ## Parameters:
    func_freq: function\n
    连续信号在频域关于omega的函数

    omega: tuple (omega1, omega2)\n
    在omega1到omega2的频域区间上，对信号频谱采样

    K: int\n
    频域上的采样数

    t: class 'numpy.array'\n
    计算t对应区间上信号的值

    ## Return
    result: class 'numpy.ndarray'\n
    result.shape == (len(t), 1), 为信号时域上在所规定区间上的值
    """
    omega1, omega2 = omega
    # delta_omega = (omega2 - omega1) / (K - 1)
    omega_freq = np.linspace(omega1, omega2, num=K)
    f_freq = np.zeros_like(omega_freq)
    for i in range(0, len(omega_freq)):
        f_freq[i] = func_freq(omega_freq[i])
    # f = 1 / (2 * pi) * delta_omega * np.asmatrix(f_freq) *\
    #     np.exp(1j * np.asmatrix(omega_freq).T * np.asmatrix(t))
    # result = np.asarray(f).reshape((len(t),))
    result = FT_pack.istft(f_freq + f_freq * 0j, omega_freq, omega, K, t)
    return result


def dtft(f, N, omega=np.linspace(-3 * pi, 3 * pi, num=1000)):
    """
    离散时间信号傅里叶变换

    ## Parameters:
    f: class 'numpy.ndarray'\n
    离散信号序列

    N: int\n
    信号采样范围,从-N到N区间上的信号值

    omega: class 'numpy.array'\n
    计算omega对应区间上信号的频谱

    ## Return
    result: class 'numpy.ndarray'\n
    result.shape == (len(omega), 1), 为信号频域上在所规定区间上频谱的值
    """
    n = np.linspace(-N, N, num=2 * N + 1)
    # f_freq = np.asmatrix(f) *\
    #     np.exp(-1j * np.asmatrix(n).T * np.asmatrix(omega))
    # result = np.asarray(f_freq).reshape((len(omega),))
    result = FT_pack.stft(f, n, (-N, N), 2 * N + 1, omega)
    return result


def idtft(func_freq, omega=(-5 * pi, 5 * pi), K=1000, N=10):
    """
    离散时间信号频谱的傅里叶逆变换

    ## Parameters:
    func_freq: function\n
    连续信号在频域关于omega的函数

    omega: tuple (omega1, omega2)\n
    在omega1到omega2的频域区间上，对信号频谱采样

    K: int\n
    频域上的采样数

    N: int\n
    计算-N到N区间上信号的值

    ## Return
    result: class 'numpy.ndarray'\n
    result.shape == (2 * N + 1, 1), 为信号时域上在所规定区间上的值
    """
    omega1, omega2 = omega
    # delta_omega = (omega2 - omega1) / (K - 1)
    omega_freq = np.linspace(omega1, omega2, num=K)
    f_freq = np.zeros_like(omega_freq)
    for i in range(0, len(omega_freq)):
        f_freq[i] = func_freq(omega_freq[i])
    n = np.linspace(-N, N, num=2 * N + 1)
    # f = np.asmatrix(f_freq)\
    #     * np.exp(-1j * np.asmatrix(omega_freq).T * np.asmatrix(n))\
    #     * delta_omega / (2 * pi)
    # result = np.asarray(f).reshape((len(n),))
    result = FT_pack.istft(f_freq, omega_freq, omega, K, n)
    # print(result[0])
    return result


def dft(f):
    """
    离散傅里叶变换
    ## Parameters:
    f: \n
    信号在时域上的离散序列，长度N即为连续N个采样值

    ## Return
    result: \n
    信号的离散频谱
    """
    # N = len(f)
    # f_freq = np.zeros(N, dtype=complex)
    # for k in range(0, N):
    #     for i in range(0, N):
    #         f_freq[k] += (f[i] + 0j) * np.exp(-1j * 2 * pi * k * i / N)
    f_freq = FT_pack.dft(f)
    return f_freq


def idft(F):
    """
    离散傅里叶变换
    ## Parameters:
    F: \n
    信号在频域上的离散序列，长度N即为连续N个采样值

    ## Return
    result: \n
    信号的离散频谱
    """
    # N = len(f)
    # f_freq = np.zeros(N, dtype=complex)
    # for k in range(0, N):
    #     for i in range(0, N):
    #         f_freq[k] += 1 / N * (f[i] + 0j)
    #                       * np.exp(1j * 2 * pi * k * i / N)
    f = FT_pack.idft(F)
    return f


def fftRadix2(f):
    '''
    当f的长度为2的整数次幂时，
    使用快速傅里叶变换计算DFT(基2-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log2(N) - int(log2(N)) <= 1e-9:
        return FFT.fft_radix_2(f)
    raise ValueError("{} is not an integer power of 2".format(N))


def fftRadix3(f):
    '''
    当f的长度为3的整数次幂时，
    使用快速傅里叶变换计算DFT(基3-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log(N, 3) - int(log(N, 3)) <= 1e-9:
        return FFT.fft_radix_3(f)
    raise ValueError("{} is not an integer power of 3".format(N))


def fftRadix5(f):
    '''
    当f的长度为5的整数次幂时，
    使用快速傅里叶变换计算DFT(基5-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log(N, 5) - int(log(N, 5)) <= 1e-9:
        return FFT.fft_radix_5(f)
    raise ValueError("{} is not an integer power of 5".format(N))


def fftRadix7(f):
    '''
    当f的长度为7的整数次幂时，
    使用快速傅里叶变换计算DFT(基7-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log(N, 7) - int(log(N, 7)) <= 1e-9:
        return FFT.fft_radix_7(f)
    raise ValueError("{} is not an integer power of 7".format(N))


def fftRadix11(f):
    '''
    当f的长度为11的整数次幂时，
    使用快速傅里叶变换计算DFT(基11-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log(N, 11) - int(log(N, 11)) <= 1e-9:
        return FFT.fft_radix_11(f)
    raise ValueError("{} is not an integer power of 11".format(N))


def fftRadix13(f):
    '''
    当f的长度为13的整数次幂时，
    使用快速傅里叶变换计算DFT(基13-FFT)

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    N = len(f)
    if log(N, 13) - int(log(N, 13)) <= 1e-9:
        return FFT.fft_radix_13(f)
    raise ValueError("{} is not an integer power of 13".format(N))


def fftMixedRadix(f):
    '''
    对离散序列f按照混合基快速傅里叶变换计算DFT

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    return FFT.fft_mix_radix(f)


def fft(f):
    '''
    对离散序列f使用快速傅里叶变换计算DFT

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    return FFT.fft(f)


def ifft(F):
    '''
    对离散序列f使用快速傅里叶变换计算IDFT

    ## Parameters:
    F: 待求fft的离散时间序列

    ## Return:
    f: class 'numpy.array'\n
    f做ifft后的结果, 为复数数组
    '''
    return FFT.ifft(F)


def fftShift(F):
    '''
    调整FFT后零点的位置至中间

    ## Parameters:
    F:\n
    进行FFT后得到的序列

    ## Return:
    shiftedF:\n
    调整后得到的序列
    '''
    return FFT.fft_hift(F)


def fftFilledToRadix2(f):
    '''
    使用快速傅里叶变换计算序列f的DFT\n
    若f的长度不是2的整数次幂，则在其末尾补零至大于其长度的最小2的整数次幂

    ## Parameters:
    f: 待求fft的离散时间序列

    ## Return:
    F: class 'numpy.array'\n
    f做fft后的结果, 为复数数组
    '''
    return FFT.fft_filledToRadix2(f)


# TODO: 傅里叶逆变换的FFT
