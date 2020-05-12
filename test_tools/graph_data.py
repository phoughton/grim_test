import sys
sys.path.append('../')
from decimal import Decimal
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from grim import mean_tester

x = []
y = []
z = []


def draw_graph(raw_x, raw_y):

    marker_y = int(100*(float(raw_y) % 1))
    marker_x = int(raw_x)

    for decimal_number in range(0, 100):
        for sample_size in range(1, 101):
            mean = f"0.{decimal_number:02d}"

            x.append(sample_size)
            y.append(float(mean))
            if mean_tester.consistency_check(mean, Decimal(sample_size)):
                z.append(1)
            else:
                z.append(0)

    results = pd.DataFrame({'x': x, 'y': y, 'z': z})
    print(results.head(1000).tail())
    pivotted = results.pivot('y', 'x', 'z')
    print(pivotted.head(1000).tail())

    ax = sns.heatmap(pivotted, cmap=sns.color_palette(["#888888", "#0000FF"]), xticklabels=1, yticklabels=2, cbar=False, linewidths=0.005, linecolor='white')
    ax.invert_yaxis()
    ax.set(xlabel="Sample Size      (Blue=Consistent  Grey=Inconsistent)", ylabel="Mean (between 0 and 1)")

    ax.hlines([marker_y], xmax=marker_x, xmin=0)
    ax.vlines([marker_x], ymax=marker_y+1, ymin=0)
    ax.hlines([marker_y+1], xmax=marker_x, xmin=0)
    ax.vlines([marker_x-1], ymax=marker_y+1, ymin=0)
    print(f"Markers. X: {marker_x}, Y: {marker_y}")
    print(mean_tester.consistency_check((Decimal(raw_y) % 1), raw_x))
    plt.show()


draw_graph('20', '1.28')
