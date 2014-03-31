from matplotlib import pyplot as plt
from skimage import (io, color)

fig, axes = plt.subplots(1, 3, figsize=(8, 3))
images = [io.imread('fig_pl%i.png' % i) for i in range(1, 4)]
titles = ['normal photograph', 'photoluminescence', 'processed']

for ax, im, ti in zip(axes, images, titles):
    ax.imshow(color.gray2rgb(im), interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(ti)

plt.tight_layout()
plt.savefig('fig_pl.png', bbox_inches='tight', dpi=600)
