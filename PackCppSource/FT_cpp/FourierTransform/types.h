#ifndef TYPES_H_
#define TYPES_H_

#include <complex>
#include <vector>
#include <Eigen/Dense>

typedef std::vector<double> vect_d;
typedef std::complex<double> complex_d;
typedef Eigen::Matrix<double, 1, Eigen::Dynamic> eg_vect_1xd;
typedef Eigen::Matrix<complex_d, 1, Eigen::Dynamic> eg_vect_complex_1xd;
typedef Eigen::Matrix<complex_d, Eigen::Dynamic, Eigen::Dynamic> eg_mat_complex_xxd;

#endif // ! TYPES_H_