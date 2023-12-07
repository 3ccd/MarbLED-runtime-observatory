import numpy as np
from matplotlib import pyplot as plt
import glob
import os


plot_list = [4, 5, 6, 7, 8]


def vis(path):
    plt.close()
    data = np.loadtxt(path)

    x = list(range(data.shape[0]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    for i in plot_list:
        y = data[:, i]
        ax.plot(x, y)

    ax.legend(plot_list)

    ah = fig.add_subplot(1, 2, 2)
    ah.hist(data[:, :18].flatten(), bins=30)

    plt.title(os.path.basename(path))
    plt.show()


if __name__ == "__main__":
    fl = glob.glob("temp/filter_cover-off_marble-on_IR-on_1701319273.1942773/*.csv")

    for file in fl:
        vis(file)
