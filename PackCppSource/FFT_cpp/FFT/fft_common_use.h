#pragma once

#ifndef FFT_COMMON_USE_H_
#define FFT_COMMON_USE_H_

#include "types.h"

#ifndef PI
#define PI 3.141592653589793
#endif

extern complex_d w31;
extern complex_d w32;

extern complex_d w51;
extern complex_d w52;
extern complex_d w53;
extern complex_d w54;

extern complex_d w71;
extern complex_d w72;
extern complex_d w73;
extern complex_d w74;
extern complex_d w75;
extern complex_d w76;

extern complex_d w11_1;
extern complex_d w11_2;
extern complex_d w11_3;
extern complex_d w11_4;
extern complex_d w11_5;
extern complex_d w11_6;
extern complex_d w11_7;
extern complex_d w11_8;
extern complex_d w11_9;
extern complex_d w11_10;

extern complex_d w13_1;
extern complex_d w13_2;
extern complex_d w13_3;
extern complex_d w13_4;
extern complex_d w13_5;
extern complex_d w13_6;
extern complex_d w13_7;
extern complex_d w13_8;
extern complex_d w13_9;
extern complex_d w13_10;
extern complex_d w13_11;
extern complex_d w13_12;

complex_d calculate_W(int N, int k);

#endif  // ! FFT_COMMON_USE_H_