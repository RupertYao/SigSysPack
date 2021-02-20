#include "fft_radix5.h"

#include "fft_common_use.h"

vect_complex_d fft_radix_5(vect_complex_d& f)
{
    int N = f.size();
    vect_complex_d F(N);
    if (N == 5)
    {
        F[0] = f[0] + f[1] + f[2] + f[3] + f[4];
        F[1] = f[0] + complex_d(0.30901699437494745, -0.9510565162951535) * f[1] + complex_d(-0.8090169943749473, -0.5877852522924732) * f[2] + complex_d(-0.8090169943749475, 0.587785252292473) * f[3] + complex_d(0.30901699437494723, 0.9510565162951536) * f[4];
        F[2] = f[0] + complex_d(-0.8090169943749473, -0.5877852522924732) * f[1] + complex_d(0.30901699437494723, 0.9510565162951536) * f[2] + complex_d(0.30901699437494745, -0.9510565162951535) * f[3] + complex_d(-0.8090169943749475, 0.587785252292473) * f[4];
        F[3] = f[0] + complex_d(-0.8090169943749475, 0.587785252292473) * f[1] + complex_d(0.30901699437494745, -0.9510565162951535) * f[2] + complex_d(0.30901699437494723, 0.9510565162951536) * f[3] + complex_d(-0.8090169943749473, -0.5877852522924732) * f[4];
        F[4] = f[0] + complex_d(0.30901699437494723, 0.9510565162951536) * f[1] + complex_d(-0.8090169943749475, 0.587785252292473) * f[2] + complex_d(-0.8090169943749473, -0.5877852522924732) * f[3] + complex_d(0.30901699437494745, -0.9510565162951535) * f[4];
        return F;
    }
    int limit = N / 5;
    vect_complex_d f_1(limit), f_2(limit), f_3(limit),
        f_4(limit), f_5(limit);
    for (int r = 0; r < limit; r++)
    {
        f_1[r] = f[5 * r];
        f_2[r] = f[5 * r + 1];
        f_3[r] = f[5 * r + 2];
        f_4[r] = f[5 * r + 3];
        f_5[r] = f[5 * r + 4];
    }
    vect_complex_d F_1, F_2, F_3,
        F_4, F_5;
    F_1 = fft_radix_5(f_1);
    F_2 = fft_radix_5(f_2);
    F_3 = fft_radix_5(f_3);
    F_4 = fft_radix_5(f_4);
    F_5 = fft_radix_5(f_5);
    for (int k = 0; k < limit; k++)
    {
        complex_d W1 = calculate_W(N, k);
        complex_d W2 = calculate_W(N, 2 * k);
        complex_d W3 = calculate_W(N, 3 * k);
        complex_d W4 = calculate_W(N, 4 * k);
        F[k] = F_1[k] + W1 * F_2[k] + W2 * F_3[k] + W3 * F_4[k] + W4 * F_5[k];
        F[k + limit] = F_1[k] + w51 * W1 * F_2[k] + w52 * W2 * F_3[k] + w53 * W3 * F_4[k] + w54 * W4 * F_5[k];
        F[k + 2 * limit] = F_1[k] + w52 * W1 * F_2[k] + w54 * W2 * F_3[k] + w51 * W3 * F_4[k] + w53 * W4 * F_5[k];
        F[k + 3 * limit] = F_1[k] + w53 * W1 * F_2[k] + w51 * W2 * F_3[k] + w54 * W3 * F_4[k] + w52 * W4 * F_5[k];
        F[k + 4 * limit] = F_1[k] + w54 * W1 * F_2[k] + w53 * W2 * F_3[k] + w52 * W3 * F_4[k] + w51 * W4 * F_5[k];
    }
    return F;
}
