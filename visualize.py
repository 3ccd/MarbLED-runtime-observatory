import numpy as np
from matplotlib import pyplot as plt
import glob
import os


def vis(path):
    plt.close()
    data = np.loadtxt(path)

    x = list(range(data.shape[0]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    for i in range(18):
        y = data[:, i]
        ax.plot(x, y)

    ah = fig.add_subplot(1, 2, 2)
    ah.hist(data[:, :18].flatten(), bins=30)

    plt.title(path)
    plt.show()


if __name__ == "__main__":
    fl = glob.glob("temp/cover-off_marble-on_IR-on_1701013089.88007/*.csv")

    for file in fl:
        vis(file)
