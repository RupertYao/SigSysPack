#include "ifft.h"
#include "fft.h"

vect_complex_d ifft(vect_complex_d& F)
{
    vect_complex_d f;
    unsigned int N = F.size();
    for (unsigned int i = 0; i < N; i++)
    {
        F[i] = std::conj(F[i]);
    }
    f = fft(F);
    for (unsigned int i = 0; i < N; i++)
    {
        f[i] = std::conj(f[i]) / double(N);
    }
    return f;
}
