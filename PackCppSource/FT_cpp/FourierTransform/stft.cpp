#include "stft.h"

eg_vect_complex_1xd stft(eg_vect_complex_1xd& f, eg_vect_1xd& fun_t,vect_d& t, unsigned int N, eg_vect_1xd& omega)
{
    double delta_t = (t[1] - t[0]) / (N - 1);
    eg_vect_complex_1xd f_freq;
    f_freq = delta_t * f * ((complex_d(0, -1) * fun_t.transpose() * omega).array().exp()).matrix();
    return f_freq;
}
