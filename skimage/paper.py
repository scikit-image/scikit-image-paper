import matplotlib.pyplot as plt
import os

figure_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), './figures'
    )


def savefig(*args, **kwargs):
    args = list(args)
    args[0] = os.path.join(figure_path, args[0])
    plt.savefig(*args, **kwargs)
