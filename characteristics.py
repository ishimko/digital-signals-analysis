import math


EXPECTED_ROOT_MEAN_SQUARE = 0.707
EXPECTED_AMPLITUDE = 1


def amplitude_by_fourier(values):
    values = list(values)
    N = len(values)
    sin_sum, cos_sum = 0, 0
    for i, y in enumerate(values):
        angle = 2 * math.pi * i / N
        sin_sum += y * math.sin(angle)
        cos_sum += y * math.cos(angle)
    sin_sum *= 2/N
    cos_sum *= 2/N
    return math.sqrt(sin_sum**2 + cos_sum**2)


def root_mean_square_with_constant_component(values):
    values = list(values)
    N = len(values)
    return math.sqrt(1 / (N + 1) * sum(x**2 for x in values))


def root_mean_square_without_constant_component(values):
    values = list(values)
    N = len(values)
    return math.sqrt(1 / (N + 1) * sum(x**2 for x in values) - (1 / (N + 1) * sum(values))**2)


def error_by_m(signal, N, K_from_N, actual_calculator, expected):
    K = K_from_N(N)
    xs = []
    ys = []
    for M in range(K, 2*N):
        xs.append(M)
        ys.append(expected - actual_calculator(list(signal(N, M))))
    return xs, ys
