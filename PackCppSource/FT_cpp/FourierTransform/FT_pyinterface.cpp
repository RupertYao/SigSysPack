#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/eigen.h>

#include "stft.h"
#include "istft.h"
#include "dft.h"
#include "idft.h"

namespace py = pybind11;

PYBIND11_MODULE(FT_pack, m)
{
    m.doc() = "傅里叶变换的辅助数值计算库";
    m.def("stft", &stft, "DTFT", py::arg("f"), py::arg("fun_t"), py::arg("t"), py::arg("N"), py::arg("omega"));
    m.def("istft", &istft, "IDTFT", py::arg("f_freq"), py::arg("omega_freq"), py::arg("omega"), py::arg("K"), py::arg("t"));
    m.def("dft", &dft, "DFT", py::arg("f"));
    m.def("idft", &idft, "IDFT", py::arg("f_freq"));
}
