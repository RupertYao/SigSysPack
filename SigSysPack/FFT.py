from .pack import FFT_pack

import numpy as np
from math import log2


def fft_radix_2(x):
    '''
    当x的长度为2的整数次幂时，
    使用快速傅里叶变换计算DFT(基2-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_2(x))


def fft_radix_3(x):
    '''
    当x的长度为3的整数次幂时，
    使用快速傅里叶变换计算DFT(基3-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_3(x))


def fft_radix_5(x):
    '''
    当x的长度为5的整数次幂时，
    使用快速傅里叶变换计算DFT(基5-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_5(x))


def fft_radix_7(x):
    '''
    当x的长度为7的整数次幂时，
    使用快速傅里叶变换计算DFT(基7-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_7(x))


def fft_radix_11(x):
    '''
    当x的长度为11的整数次幂时，
    使用快速傅里叶变换计算DFT(基11-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_11(x))


def fft_radix_13(x):
    '''
    当x的长度为13的整数次幂时，
    使用快速傅里叶变换计算DFT(基13-FFT)

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_radix_13(x))


def fft_filledToRadix2(x):
    '''
    使用快速傅里叶变换计算序列x的DFT\n
    若x的长度不是2的整数次幂，则在其末尾补零至大于其长度的最小2的整数次幂

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    N = len(x)
    log2N = log2(N)
    # print(log2N, 2 ** (int(log2N) + 1))
    if log2N - int(log2N) <= 1e-9:
        X = fft_radix_2(x)
    else:
        x_ = np.zeros(2 ** (int(log2N) + 1))
        for i in range(0, N):
            x_[i] = x[i]
        print(len(x_))
        X = fft_radix_2(x_)
    return X[:N]


def fft_mix_radix(x):
    '''
    通用混合基FFT(当出现适用于单一基FFT的情况时，不会直接选择对应单一基FFT)\n
    使用快速傅里叶变换计算序列x的DFT\n

    ## Parameters:
    x: 待求fft的离散时间序列

    ## Return:
    X: class 'numpy.array'\n
    x做fft后的结果, 为复数数组
    '''
    return np.array(FFT_pack.fft_mix_radix(x))


def fft(x):
    return np.array(FFT_pack.fft(x))


def ifft(X):
    '''
    NOTE:
    这里的ifft并没有专门编写对应的程序，而是利用
    x(n) = 1/N{DFT[X*(k)]}*
    (*表示共轭)
    的性质，直接共用现有的fft程序，完成计算
    '''
    # X = np.array(X)
    # x = np.conj(np.array(FFT_pack.fft(np.conj(X)))) / len(X)
    x = np.array(FFT_pack.ifft(X))
    return x


def fft_shift(F):
    '''
    调整FFT后零点的位置至中间

    ## Parameters:
    F:\n
    进行FFT后得到的序列

    ## Return:
    shiftedF:\n
    调整后得到的序列
    '''
    return np.array(FFT_pack.fft_shift(F))
