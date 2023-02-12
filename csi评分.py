import numpy as np


def get_CSI(pred, label, threshold=30):
    hit = np.sum((pred > threshold) * (label > threshold))
    far = np.sum((pred > threshold) * (label < threshold))
    miss = np.sum((pred < threshold) * (label > threshold))
    # corn = np.sum((pred < threshold) * (label < threshold))
    CSI = hit / (hit + far + miss + 1e-6)  # max
    return CSI
