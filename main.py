import cmath
from signal import signal

from matplotlib import pyplot as plt
from numpy import fft

from fourier import amplitude_by_fourier


def main():
    print(amplitude_by_fourier(list(signal(64))))


if __name__ == '__main__':
    main()
