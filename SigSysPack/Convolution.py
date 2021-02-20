import numpy as np

from .pack import Conv_pack


def convolution(vector_a, vector_b):
    """
    计算两个离散序列的卷积和
    ## Parameters:
    vector_a, vector_b: list\n
        两个离散序列

    ## Return:
    result: list\n
        卷积的结果
    """
    # len_a = len(vector_a)
    # len_b = len(vector_b)
    # len_res = len_a + len_b - 1
    # result = [0] * len_res

    # for n in range(0, len_res):
    #     for k in range(0, len_a):
    #         vect_b_index = n - k
    #         if vect_b_index >= 0 and vect_b_index < len_b:
    #             result[n] += vector_a[k] * vector_b[vect_b_index]
    # return result
    result = Conv_pack.conv(vector_a, vector_b)
    if isinstance(vector_a[0], complex) or isinstance(vector_b[0], complex):
        return result
    return np.real(result)


def convolutionIntegral(func1, func2,
                        tlim1=(-5, 5), tlim2=(-5, 5), delta=0.01):
    """
    计算连续时间信号的卷积积分
    ## Parameters
    func1, func2: function\n
    需要计算卷积积分的两个函数

    tlim1, tlim2: tuple\n
    两个函数的取样范围

    delta: float
    取样的间隔

    ## Return
    (t_result, result):\n
    t_result: 计算结果对应的时间\n
    result: 计算的结果
    """
    # 计算f1的取样值
    t11, t12 = tlim1
    n1 = int((t12 - t11) / delta)
    t1 = [t11 + delta * i for i in range(0, n1 + 1)]
    f1 = [func1(i) for i in t1]
    # 计算f2的取样值
    t21, t22 = tlim2
    n2 = int((t22 - t21) / delta)
    t2 = [t21 + delta * i for i in range(0, n2 + 1)]
    f2 = [func2(i) for i in t2]
    # 计算卷积
    result = convolution(f1, f2)
    for i in range(0, len(result)):
        result[i] = result[i] * delta
    n = len(result)
    t_result = [i * delta + (t11 + t21) for i in range(0, n)]

    return t_result, result


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1, 2, 3, 4]
    a = np.random.randn(5)
    # print(a)
    c = convolution(a, b)
    print(c)

    def func1(t):
        if abs(t) <= 0.5:
            return 1
        else:
            return 0

    def func2(t):
        if abs(t) <= 1:
            return 1
        else:
            return 0

    t_res, res = convolutionIntegral(func1=func1, func2=func2)
    import matplotlib.pyplot as plt
    plt.plot(t_res, res)
    plt.show()
