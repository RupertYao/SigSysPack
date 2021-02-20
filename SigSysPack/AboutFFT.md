# About FFT Module

使用门函数:
```python
def Gate(tao, t):
    if np.abs(t) <= np.abs(tao) / 2:
        return 1
    else:
        return 0
```
对FFT模块中的几个主要函数进行运行时间测试，并与FourierTransform模块中的dft进行对比，测试环境:

|项目|详情|
|:--:|:--:|
|CPU|Intel(R) Core(TM) i5-9300H @2.40GHz|
|内存|16.0 GB|
|操作系统|版本: Windows 10 家庭中文版;<br>版本号: 20H2;<br>操作系统版本: 19042.746|
|Python|3.8.3|


得到具体情况如下:

1. 10000个采样点，测试`FFT.fft()`、`FFT.fft_common()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|361.031250s|
   |FFT.fft()|0.218750s|
   |FFT.fft_common()|0.218750s|

2. 16384个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_2()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|983.015625s|
   |FFT.fft()|0.437500s|
   |FFT.fft_common()|0.437500s|
   |FFT.fft_2()|0.406250s|

3. 19683个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_3()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|1418.484375s|
   |FFT.fft()|0.500000s|
   |FFT.fft_common()|0.421875s|
   |FFT.fft_3()|0.437500s|

4. 15625个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_5()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|897.625000s|
   |FFT.fft()|0.328125s|
   |FFT.fft_common()|0.328125s|
   |FFT.fft_5()|0.359375s|

5. 16807个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_7()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|1028.218750s|
   |FFT.fft()|0.390625s|
   |FFT.fft_common()|0.359375s|
   |FFT.fft_7()|0.406250s|

6. 14641个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_11()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|779.328125s|
   |FFT.fft()|0.375000s|
   |FFT.fft_common()|0.375000s|
   |FFT.fft_11()|0.375000s|

7. 28561个采样点，测试`FFT.fft()`、`FFT.fft_common()`、`FFT.fft_13()`以及`FourierTransform.dft()`得到:
   
   |Function|Spend Time|
   |:--:|:--:|
   |FourierTransform.dft()|2973.812500s|
   |FFT.fft()|0.890625s|
   |FFT.fft_common()|0.890625s|
   |FFT.fft_13()|0.875000s|

## 测试代码:
```python
import numpy as np
import time

import FFT
import FourierTransform as FT


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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    # 16384 Samples
    f_log.write("16384 Samples:\n")
    t = np.linspace(0, 2**14 - 1, num=2**14)
    f = np.zeros_like(t)
    for i in range(0, len(t)):
        f[i] = Gate(4, t[i])
    start = time.process_time()
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_2(f)
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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_3(f)
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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_5(f)
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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_7(f)
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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_11(f)
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
    F = FT.dft(f)
    end = time.process_time()
    f_log.write("DFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_common(f)
    end = time.process_time()
    f_log.write("Common FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft(f)
    end = time.process_time()
    f_log.write("FFT Spend {:f}s\n".format(end - start))
    start = time.process_time()
    F = FFT.fft_13(f)
    end = time.process_time()
    f_log.write("FFT_13 Spend {:f}s\n".format(end - start))
    f_log.write('\n')

    f_log.close()
```