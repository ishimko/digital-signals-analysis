import math


def amplitude_by_fourier(ys):
    ys = list(ys)
    N = len(ys)
    sin_sum, cos_sum = 0, 0
    for i, y in enumerate(ys):
        sin_sum += y * math.sin(2 * math.pi * i / N)
        cos_sum += y * math.cos(2 * math.pi * i / N)
    sin_sum *= 2/N
    cos_sum *= 2/N
    return math.sqrt(sin_sum**2 + cos_sum**2)
