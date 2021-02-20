#include "fft_shift.h"

#include "fft_common_use.h"

vect_complex_d fft_shift(vect_complex_d& F)
{
    unsigned int N = F.size();
    if(N == 1)
    {
        return F;
    }
    unsigned int flag_point = N / 2;
    vect_complex_d shifted_F(N);
    for (unsigned int i = flag_point; i < N; i++)
    {
        shifted_F[i - flag_point] = F[i];
    }
    for (unsigned int i = 0; i < flag_point; i++)
    {
        shifted_F[i + flag_point] = F[i];
    }
    return shifted_F;
}
