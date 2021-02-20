#ifndef STFT_H_
#define STFT_H_

#include "types.h"

eg_vect_complex_1xd stft(eg_vect_complex_1xd& f, eg_vect_1xd& fun_t, vect_d& t, unsigned int N, eg_vect_1xd& omega);

#endif // ! STFT_H_