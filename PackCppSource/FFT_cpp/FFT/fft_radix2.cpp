#include "fft_radix2.h"

#include "fft_common_use.h"

vect_complex_d fft_radix_2(vect_complex_d& f)
{
    int N = f.size();
    vect_complex_d F(N);
    if(N == 2)
    {
        F[0] = f[0] + f[1];
        F[1] = f[0] - f[1];
        return F;
    }
    int limit = N / 2;
    vect_complex_d f_1(limit), f_2(limit);
    for(int r = 0; r < limit; r++)
    {
        f_1[r] = f[2 * r];
        f_2[r] = f[2 * r + 1];
    }
    vect_complex_d F_1, F_2;
    F_1 = fft_radix_2(f_1);
    F_2 = fft_radix_2(f_2);
    for(int k = 0; k < limit; k++)
    {
        complex_d W = calculate_W(N, k);
        F[k] = F_1[k] + W * F_2[k];
        F[k + limit] = F_1[k] - W * F_2[k];
    }
    return F;
}
