#include "fft.h"

#include "fft_common_use.h"
#include "fft_radix2.h"
#include "fft_radix3.h"
#include "fft_radix5.h"
#include "fft_radix7.h"
#include "fft_radix11.h"
#include "fft_radix13.h"
#include "fft_mix_radix.h"

const double err_precision = 1e-6;

vect_complex_d fft(vect_complex_d& f)
{
    unsigned int N = f.size();
    double logN = log2(N);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_2(f);
    }
    logN = log(N) / log(3);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_3(f);
    }
    logN = log(N) / log(5);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_5(f);
    }
    logN = log(N) / log(7);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_7(f);
    }
    logN = log(N) / log(11);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_11(f);
    }
    logN = log(N) / log(13);
    if (logN - int(logN + err_precision) <= err_precision)
    {
        return fft_radix_13(f);
    }
    return fft_mix_radix(f);
}
