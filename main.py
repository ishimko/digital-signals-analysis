import math
from signal import harmonic_signal

from matplotlib import pyplot as plt

from characteristics import \
    error_by_m, \
    amplitude_by_fourier, \
    root_mean_square_with_constant_component, \
    root_mean_square_without_constant_component, \
    EXPECTED_AMPLITUDE, \
    EXPECTED_ROOT_MEAN_SQUARE
from drawer import plot_section


N = 64
K_FROM_N = lambda N: N // 4
PHASES = {
    '0': 0,
    r'\pi/2': math.pi / 2
}
LABELS = [
    'Amplitude error',
    'Root mean sqaure with constant component',
    'Root mean sqaure without constant component'
]


def main():
    lines = []

    plt.subplots_adjust(top=0.8)

    for i, phase_description in enumerate(PHASES.items()):
        phase_repr, phase = phase_description
        plt.subplot(1, 2, i+1)
        signal = lambda N, M: harmonic_signal(N, M, phase)
        error_by_m_for = lambda actual_calculator, expected: error_by_m(
            signal,
            N,
            K_FROM_N,
            actual_calculator,
            expected
        )
        plots = [
            error_by_m_for(amplitude_by_fourier, EXPECTED_AMPLITUDE),
            error_by_m_for(root_mean_square_with_constant_component, EXPECTED_ROOT_MEAN_SQUARE),
            error_by_m_for(root_mean_square_without_constant_component, EXPECTED_ROOT_MEAN_SQUARE)
        ]
        lines = plot_section(plots, '$f={}$'.format(phase_repr))

    plt.figlegend(lines, LABELS, loc='upper center')

    plt.show()


if __name__ == '__main__':
    main()
