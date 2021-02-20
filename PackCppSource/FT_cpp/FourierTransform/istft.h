#ifndef ISTFT_H_
#define ISTFT_H_

#include "types.h"

eg_vect_complex_1xd istft(eg_vect_complex_1xd& f_freq, eg_vect_1xd& omega_freq ,vect_d& omega, unsigned int K, eg_vect_1xd& t);

#endif // ! ISTFT_H_
