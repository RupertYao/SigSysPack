#include "idft.h"
#include "FT_commonuse.h"

eg_vect_complex_1xd idft(eg_vect_complex_1xd& f_freq)
{
    unsigned int N = f_freq.cols();
    eg_vect_1xd n;
    n.setLinSpaced(double(N), 0, double(N) - 1);
    eg_vect_complex_1xd f;
    f = 1 / N * f_freq * ((complex_d(0, 1) * 2.0 * PI / double(N) * n.transpose() * n).array().exp()).matrix();
    return f_freq;
}
