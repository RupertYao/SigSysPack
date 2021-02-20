#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include "fft.h"
#include "ifft.h"
#include "fft_radix2.h"
#include "fft_radix3.h"
#include "fft_radix5.h"
#include "fft_radix7.h"
#include "fft_radix11.h"
#include "fft_radix13.h"
#include "fft_mix_radix.h"
#include "fft_shift.h"

namespace py = pybind11;

PYBIND11_MODULE(FFT_pack, m)
{
    m.doc() = "fft numeric compute module";
    //函数名称， 函数指针， 描述
    m.def("fft", &fft, "FFT", py::arg("f"));
    m.def("ifft", &ifft, "IFFT", py::arg("F"));
    m.def("fft_radix_2", &fft_radix_2, "Radix2-FFT", py::arg("f"));
    m.def("fft_radix_3", &fft_radix_3, "Radix3-FFT", py::arg("f"));
    m.def("fft_radix_5", &fft_radix_5, "Radix5-FFT", py::arg("f"));
    m.def("fft_radix_7", &fft_radix_7, "Radix7-FFT", py::arg("f"));
    m.def("fft_radix_11", &fft_radix_11, "Radix11-FFT", py::arg("f"));
    m.def("fft_radix_13", &fft_radix_13, "Radix13-FFT", py::arg("f"));
    m.def("fft_mix_radix", &fft_mix_radix, "Mix-Radix-FFT", py::arg("f"));
    m.def("fft_shift", &fft_shift, "调整FFT后零点的位置至中间", py::arg("F"));
}
