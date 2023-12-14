import numpy as np
from collections import Counter, namedtuple


class NaiveBayes:
    def __init__(self, type="gaussian", alpha=1, beta=1, MLE=True):
        self.type = type.lower()
        assert self.type in [
            "gaussian",  # continuous
            "multinomial",  # discrete, count
            "bernoulli",  # discrete, binary
            "catagorical",  # discrete, multi-class
        ], "Unknown type"
        self.alpha = alpha
        self.beta = beta
        self.MLE = MLE

    def fit(self, X, y, laplace=True):
        self.X = X
        self.y = y

        if self.type == "bernoulli":
            self._fit_bernoulli(laplace)

        elif self.type == "catagorical":
            self._fit_catagorical(laplace)

        elif self.type == "multinomial":
            self._fit_count(laplace)

        elif self.type == "gaussian":
            self._fit_gaussian()

    def _fit_bernoulli(self, laplace):
        self.classes = np.unique(self.y)
        self.class_counts = Counter(self.y)
        if self.MLE:
            if laplace:
                self.class_probs = {
                    c: (self.class_counts[c] + 1) / (len(self.y) + len(self.classes))
                    for c in self.classes
                }
            self.class_probs = {
                c: self.class_counts[c] / len(self.y) for c in self.classes
            }
        else:
            if laplace:
                self.class_probs = {
                    c: (self.class_counts[c] + self.alpha)
                    / (len(self.y) + self.alpha + self.beta)
                    for c in self.classes
                }
            else:
                self.class_probs = {
                    c: (self.class_counts[c] + self.alpha - 1)
                    / (len(self.y) + self.alpha + self.beta - 2)
                    for c in self.classes
                }

    def _fit_catagorical(self, laplace):
        self.classes = np.unique(self.y)
        self.class_counts = Counter(self.y)
        if self.MLE:
            pass

    def _fit_count(self, laplace):
        self.classes = np.unique(self.y)
        self.class_counts = Counter(self.y)
        self.class_index = {c: np.where(self.y == c)[0] for c in self.classes}

    def _fit_gaussian(self):
        pass

    def predict(self, X):
        pass
