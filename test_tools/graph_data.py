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

for decimal_number in range(0, 100):
    for sample_size in range(1, 100):
        mean = f"0.{decimal_number:02d}"

        x.append(sample_size)
        y.append(float(mean))
        if mean_tester.consistency_check(mean, Decimal(sample_size)):
            z.append(1)
        else:
            z.append(0)

results = pd.DataFrame({'x': x, 'y': y, 'z': z})
pivotted = results.pivot('y', 'x', 'z')
ax = sns.heatmap(pivotted, cmap='coolwarm', xticklabels=1, yticklabels=5, cbar=False, )
ax.invert_yaxis()
ax.set(xlabel="Sample Size", ylabel="Mean (between 0 and 1)")
plt.show()
