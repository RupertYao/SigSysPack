#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>

#include "conv.h"

namespace py = pybind11;

PYBIND11_MODULE(Conv_pack, m)
{
    m.doc() = "辅助加速Python的卷积和计算";
    m.def("conv", &conv, "calculate convolution", py::arg("vector_a"), py::arg("vector_b"));
}
