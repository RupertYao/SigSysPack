#include "dft.h"
#include "FT_commonuse.h"
#include <iostream>

eg_vect_complex_1xd dft(eg_vect_complex_1xd& f)
{
    unsigned int N = f.cols();
    eg_vect_1xd n;
    n.setLinSpaced(double(N), 0, double(N) - 1);
    eg_vect_complex_1xd f_freq;
    f_freq = f * ((complex_d(0, -1) * 2.0 * PI / double(N) * n.transpose() * n).array().exp()).matrix();
    return f_freq;
}
