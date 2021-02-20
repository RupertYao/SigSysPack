#include "fft_common_use.h"

#include <cmath>

complex_d w31(-0.5, -0.8660254037844387);
complex_d w32(-0.5, 0.8660254037844385);

complex_d w51(0.30901699437494745, -0.9510565162951535);
complex_d w52(-0.8090169943749473, -0.5877852522924732);
complex_d w53(-0.8090169943749475, 0.587785252292473);
complex_d w54(0.30901699437494723, 0.9510565162951536);

complex_d w71(0.6234898018587336, -0.7818314824680298);
complex_d w72(-0.22252093395631434, -0.9749279121818236);
complex_d w73(-0.900968867902419, -0.43388373911755823);
complex_d w74(-0.9009688679024191, 0.433883739117558);
complex_d w75(-0.2225209339563146, 0.9749279121818236);
complex_d w76(0.6234898018587334, 0.7818314824680299);

complex_d w11_1(0.8412535328311812, -0.5406408174555976);
complex_d w11_2(0.41541501300188644, -0.9096319953545183);
complex_d w11_3(-0.142314838273285, -0.9898214418809328);
complex_d w11_4(-0.654860733945285, -0.7557495743542583);
complex_d w11_5(-0.9594929736144974, -0.28173255684142967);
complex_d w11_6(-0.9594929736144975, 0.2817325568414294);
complex_d w11_7(-0.6548607339452852, 0.7557495743542582);
complex_d w11_8(-0.14231483827328523, 0.9898214418809327);
complex_d w11_9(0.41541501300188605, 0.9096319953545186);
complex_d w11_10(0.8412535328311812, 0.5406408174555974);

complex_d w13_1(0.8854560256532099, -0.4647231720437685);
complex_d w13_2(0.5680647467311559, -0.8229838658936564);
complex_d w13_3(0.120536680255323, -0.992708874098054);
complex_d w13_4(-0.35460488704253545, -0.9350162426854148);
complex_d w13_5(-0.7485107481711012, -0.6631226582407952);
complex_d w13_6(-0.970941817426052, -0.23931566428755768);
complex_d w13_7(-0.9709418174260521, 0.23931566428755743);
complex_d w13_8(-0.7485107481711013, 0.663122658240795);
complex_d w13_9(-0.3546048870425359, 0.9350162426854147);
complex_d w13_10(0.1205366802553232, 0.992708874098054);
complex_d w13_11(0.5680647467311548, 0.822983865893657);
complex_d w13_12(0.88545602565321, 0.4647231720437684);

complex_d calculate_W(int N, int k)
{
    complex_d result;
    result = std::exp(complex_d(0, -1 * 2 * PI * k / N));
    return result;
}