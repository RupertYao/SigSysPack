import numpy as np
import time

from SigSysPack import FFT
import SigSysPack.FourierTransform as FT


def Gate(tao, t):
    if np.abs(t) <= np.abs(tao) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    f_log = open("./timeSpend.log", 'w', encoding='utf-8')
    # t = np.linspace(0, 999, num=1000)
    # 10000 Samples
    f_log.write("10000 Samples:\n")
    t = np.linspace(0, 9999, num=10000)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.ifft(f)
    end = time.process_time()
    f_log.write("IFFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FT.idft(f)
    end = time.process_time()
    f_log.write("IDFT Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 16384 Samples
    f_log.write("16384 Samples:\n")
    t = np.linspace(0, 2**14 - 1, num=2**14)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_2(f)
    end = time.process_time()
    f_log.write("FFT_2 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 19683 Samples
    f_log.write("19683 Samples:\n")
    t = np.linspace(0, 3**9 - 1, num=3**9)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_3(f)
    end = time.process_time()
    f_log.write("FFT_3 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 15625 Samples
    f_log.write("15625 Samples:\n")
    t = np.linspace(0, 5**6 - 1, num=5**6)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_5(f)
    end = time.process_time()
    f_log.write("FFT_5 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 16807 Samples
    f_log.write("16807 Samples:\n")
    t = np.linspace(0, 7**5 - 1, num=7**5)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_7(f)
    end = time.process_time()
    f_log.write("FFT_7 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 14641 Samples
    f_log.write("14641 Samples:\n")
    t = np.linspace(0, 11**4 - 1, num=11**4)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_11(f)
    end = time.process_time()
    f_log.write("FFT_11 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 28561 Samples
    f_log.write("28561 Samples:\n")
    t = np.linspace(0, 13**4 - 1, num=13**4)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_mix_radix(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    FFT.fft_radix_13(f)
    end = time.process_time()
    f_log.write("FFT_13 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    f_log.close()
