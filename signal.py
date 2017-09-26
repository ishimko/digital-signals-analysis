import math


def harmonic_signal(N, M, phase=0):
    for x in range(M):
        yield math.sin((2*math.pi*x)/N + phase)
