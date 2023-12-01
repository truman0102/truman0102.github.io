import numpy as np
from scipy import signal


def dftuv(M, N):
    u = np.arange(0, M)  # 生成频率域的网格
    v = np.arange(0, N)  # 生成频率域的网格
    idx = np.where(u > M / 2)  # 找到大于M/2的索引
    u[idx] = u[idx] - M  # 将大于M/2的索引减去M
    idy = np.where(v > N / 2)  # 找到大于N/2的索引
    v[idy] = v[idy] - N  # 将大于N/2的索引减去N
    [V, U] = np.meshgrid(v, u)  # 生成频率域的网格
    return U, V  # 返回频率域的网格


def lpfilter(type, M, N, D0, n=1):
    U, V = dftuv(M, N)  # 生成频率域的网格
    D = np.sqrt(U**2 + V**2)  # 计算频率域的距离
    if type == "ideal":  # 理想低通滤波器
        H = D <= D0  # 生成理想低通滤波器
    elif type == "btw":  # 巴特沃斯低通滤波器
        if n < 1:  # n必须大于1
            raise ValueError("n must be greater than 1")
        H = 1 / (1 + (D / D0) ** (2 * n))  # 生成巴特沃斯低通滤波器
    elif type == "gaussian":  # 高斯低通滤波器
        H = np.exp(-(D**2) / (2 * (D0**2)))  # 生成高斯低通滤波器
    else:  # 未知滤波器类型
        raise ValueError("Unknown filter type")
    return H  # 返回滤波器


def hpfilter(type, M, N, D0, n=1):
    Hlp = lpfilter(type, M, N, D0, n)
    H = 1 - Hlp
    return H


def imfilter(f, w, **kwargs):
    shape = f.shape  # 获取输入图像的形状
    # filetering_mode = "corr"
    filtering_mode = kwargs.get("filtering_mode", "corr")
    # boundary_options = None
    boundary_options = kwargs.get("boundary_options", None)
    # size_options = "same"
    size_options = kwargs.get("size_options", "same")
    # P = 0  # 边界填充值
    P = kwargs.get("P", 0)

    for i in kwargs.values():
        if i in ("corr", "conv"):
            # filetering_mode = i
            filtering_mode = i
        elif i in ("replicate", "circular", "symmetric"):
            boundary_options = i
        elif i in ("same", "full"):
            size_options = i
        elif isinstance(i, int, float):
            P = i
        else:
            raise ValueError("input error")
    if filtering_mode == "corr":
        w = np.fliplr(np.flipud(w))  # 卷积核翻转
    if boundary_options == "replicate":  # 使用边界值填充
        f = np.pad(f, w.shape[0] // 2, "edge")
        boundary_options = "fill"
    elif boundary_options == "circular":  # 使用循环填充
        boundary_options = "wrap"
    elif boundary_options == "symmetric":  # 使用对称填充
        boundary_options = "symm"
    elif boundary_options is None:  # 指定了边界填充值
        f = np.pad(f, w.shape[0] // 2, "constant", constant_values=P)
        boundary_options = "fill"
    f = signal.convolve2d(f, w, mode=size_options, boundary=boundary_options)
    return f[0 : shape[0], 0 : shape[1]]  # 返回滤波结果
