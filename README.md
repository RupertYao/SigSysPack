# SigSysPack

*使用C++进行底层加速的信号与系统常用操作Python工具包*

## 简介

SigSysPack提供了可以通过Python程序调用的信号与系统常用计算操作的函数接口，支持初学者进行一维信号的操作：

- 卷积
- 连续信号的傅里叶变换(STFT)
- 连续信号的傅里叶逆变换(ISTFT)
- 离散信号的傅里叶变换(DTFT)
- 离散信号的傅里叶逆变换(IDTFT)
- 离散傅里叶变换(DFT)
- 离散傅里叶逆变换(IDFT)
- 快速傅里叶变换(FFT)
- 快速傅里叶逆变换(IFFT)

## 编译使用

1. C++底层依赖于:

   - Eigen3
   - pybind11
   - 所使用Python版本对应的接口及连接库

   因此需要事先安装好这些依赖库

   此外，本工具包使用xmake作为编译管理工具，编译器选用msvc，若使用其他工具进行编译，可参照编译设置，类比自主修改。

2. 修改PackCppSource目录下的`xmake.lua`文件

   - 将`PY_INCLUDE_PATH`, `PY_LIB_PATH`路径分别修改为本机Python安装目录(或 Anaconda 所使用环境的目录)下，`Python.h`所在目录，以及`python3.lib`, `python38.lib`(`python3x.lib`)所在目录(不同的Python版本，以及操作系统，连接库的名称可能会有差别，但命名形式大致相同，可参照互联网上各类博客中对于 pybind11 使用配置时的连接路径选择)
   - 将`PYBIND11_INCLUDE_PATH`修改为本机pybind11安装目录下的include目录的路径
   - 将`EIGEN3_PATH`修改为本机Eigen3安装目录下`eigen3`目录所在路径

3. 在`xmake.lua`所在目录处打开终端或者命令行，依次执行`xmake`, `xmake install`

4. 将产生的`install`文件夹下`bin`目录，以及`lib`目录下所有文件均复制到`SigSysPack/pack`目录下

5. 将`SigSysPack`文件夹复制到需要调用该工具包的`*.py`文件同一目录下，即可在该`*.py`文件中调用工具包中的函数