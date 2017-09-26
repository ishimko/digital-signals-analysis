from matplotlib import pyplot as plt


def plot_section(plots, title):
    lines = []
    for plot in plots:
        lines.append(plt.plot(*plot)[0])
    return lines
