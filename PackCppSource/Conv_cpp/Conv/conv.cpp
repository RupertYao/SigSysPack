#include "conv.h"

vect_complex_d conv(vect_complex_d& vector_a, vect_complex_d& vector_b)
{
    int len_a = vector_a.size();
    int len_b = vector_b.size();
    int len_res = len_a + len_b - 1;
    vect_complex_d result(len_res);

    int vect_b_index;
    for (int n = 0; n < len_res; n++)
    {
        result[n] = 0;
        for (int k = 0; k < len_a; k++)
        {
            vect_b_index = n - k;
            if (vect_b_index >= 0 && vect_b_index < len_b)
            {
                result[n] += vector_a[k] * vector_b[vect_b_index];
            }
        }
    }
    return result;
}
