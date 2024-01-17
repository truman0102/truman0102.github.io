import numpy as np


def y_to_array(y):
    if isinstance(y, (list, tuple)):
        y = np.array(y)
    elif isinstance(y, np.ndarray):
        pass
    else:
        raise ValueError("y must be a list, tuple or numpy array")
    assert y.ndim == 1
    return y


def euclidean_distance(x1, x2):
    """
    :param x1: vector 1, 1D or 2D array
    :param x2: vector 2, 1D or 2D array
    :return: euclidean distance between x1 and x2
    """
    if x1.ndim == 1:
        x1 = x1.reshape(1, -1)
    if x2.ndim == 1:
        x2 = x2.reshape(1, -1)
    assert x1.shape[1] == x2.shape[1]
    return np.sqrt(np.sum((x1 - x2) ** 2, axis=1))


def silhouette_score(X, labels, samples=None, index=None):
    """
    :param X: data matrix (n_samples, n_features)
    :param labels: cluster labels (n_samples,)
    :param samples: samples to calculate silhouette score
    :param index: index of sample to calculate silhouette score
    :return: silhouette score

    - If samples is None and index is None, calculate silhouette score for all samples.
    - If index is not None, calculate silhouette score for sample at index and ignore samples.
    - If samples is not None and index is None, calculate silhouette score for samples.
        - samples can be a 1D array or a 2D array.
        - If samples is a 1D array, convert it to a 2D array.
        - All samples must belong to X.
    """
    assert X.ndim == 2  # X must be a 2D array
    labels = y_to_array(labels)
    assert (
        labels.shape[0] == X.shape[0]
    )  # number of labels must equal number of samples

    if index is not None:  # 如果指定了index，那么就只计算index对应的样本的轮廓系数
        index = y_to_array(index)
    elif samples is not None:  # 如果指定了samples，那么就只计算samples对应的样本的轮廓系数
        if samples.ndim == 1:
            samples = samples.reshape(1, -1)
        assert samples.ndim == 2
        index = np.where(np.all(X == samples[:, None], axis=2))[1]  # 找到samples在X中的索引
    else:  # 如果没有指定index和samples，那么就计算所有样本的轮廓系数
        index = np.arange(X.shape[0])  # 所有样本的索引

    custers = {label: np.where(labels == label)[0] for label in np.unique(labels)}

    silhouette_scores = []

    for i in index:
        a = np.mean(
            euclidean_distance(X[i], X[[j for j in custers[labels[i]] if j != i]])
            # [euclidean_distance(X[i], X[j]) for j in custers[labels[i]] if j != i]
        )
        b = np.min(
            [
                np.mean(
                    # [euclidean_distance(X[i], X[j]) for j in custers[label]]
                    euclidean_distance(X[i], X[custers[label]])
                )  # 计算样本i与其他类别的平均距离
                for label in custers  # 遍历所有与样本i不同的类别
                if label != labels[i]
            ]
        )  # 找到与样本i不同的类别中，与样本i距离最近的类别的平均距离
        silhouette_scores.append((b - a) / max(a, b))

    return np.mean(silhouette_scores)
