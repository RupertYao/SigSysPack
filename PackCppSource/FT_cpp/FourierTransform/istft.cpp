#include "istft.h"
#include "FT_commonuse.h"

eg_vect_complex_1xd istft(eg_vect_complex_1xd& f_freq, eg_vect_1xd& omega_freq ,vect_d& omega, unsigned int K, eg_vect_1xd& t)
{
    double delta_omega = (omega[1] - omega[0]) / (K - 1);
    eg_vect_complex_1xd f;
    f = 1 / (2 * PI) * (delta_omega * f_freq * ((complex_d(0, 1) * omega_freq.transpose() * t).array().exp()).matrix());
    return f;
}