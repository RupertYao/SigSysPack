#include "fft_radix3.h"

#include "fft_common_use.h"

vect_complex_d fft_radix_3(vect_complex_d& f)
{
    int N = f.size();
    vect_complex_d F(N);
    if(N == 3)
    {
        F[0] = f[0] + f[1] + f[2];
        F[1] = f[0] + complex_d(-0.5, -0.8660254037844387) * f[1]\
            + complex_d(-0.5, 0.8660254037844385) * f[2];
        F[2] = f[0] + complex_d(-0.5, 0.8660254037844385) * f[1] \
            + complex_d(-0.5, -0.8660254037844387) * f[2];
        return F;
    }
    int limit = N / 3;
    vect_complex_d f_1(limit), f_2(limit), f_3(limit);
    for(int r = 0; r < limit; r++)
    {
        f_1[r] = f[3 * r];
        f_2[r] = f[3 * r + 1];
        f_3[r] = f[3 * r + 1];
    }
    vect_complex_d F_1, F_2, F_3;
    F_1 = fft_radix_3(f_1);
    F_2 = fft_radix_3(f_2);
    F_3 = fft_radix_3(f_3);
    for(int k = 0; k < limit; k++)
    {
        complex_d W1 = calculate_W(N, k);
        complex_d W2 = calculate_W(N, 2 * k);
        F[k] = F_1[k] + W1 * F_2[k] + W2 * F_3[k];
        F[k + limit] = F_1[k] + w31 * W1 * F_2[k] + w32 * W2 * F_3[k];
        F[k + 2 * limit] = F_1[k] + w32 * W1 * F_2[k] + w31 * W2 * F_3[k];
    }
    return F;
}
